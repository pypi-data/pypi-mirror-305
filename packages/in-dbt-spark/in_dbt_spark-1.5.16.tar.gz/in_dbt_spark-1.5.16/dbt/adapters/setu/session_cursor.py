import os
import time
from typing import Optional

import dbt.exceptions
from dbt.adapters.setu.client import SetuClient
from dbt.events import AdapterLogger
from dbt.adapters.setu.constants import VALID_STATEMENT_KINDS
from dbt.adapters.setu.models import StatementKind, Output, StatementState, Statement
from dbt.adapters.setu.utils import (
    polling_intervals,
    waiting_for_output,
    get_data_from_json_output,
)

logger = AdapterLogger("Spark")


class SetuStatementCursor:
    """
    Manage SETU statement and high-level interactions with it.
    :param client: setu client for managing statements
    :param session_id: setu session ID
    :param kafka_topic: Topic name to send data to kafka
    :param kafka_broker_url: Broker to send data to kafka
    """

    def __init__(
        self,
        client: SetuClient,
        session_id: str,
        kafka_topic: Optional[str] = None,
        kafka_broker_url: Optional[str] = None,
    ):
        self.session_id: str = session_id
        self.client: SetuClient = client
        self.statement: Optional[Statement] = None
        self.kafka_topic: Optional[str] = kafka_topic
        self.kafka_broker_url: Optional[str] = kafka_broker_url

    def description(self):
        self.fetchall()
        json_output = self.statement.output.json
        columns = json_output["schema"]["fields"]

        # Old behavior but with an added index field["type"]
        return [[column["name"], column["type"]] for column in columns]

    def execute(self, code: str) -> Output:
        """
        :param code:
        :return:
        """
        statement_kind: StatementKind = self.get_statement_kind(
            code, self.kafka_topic, self.kafka_broker_url
        )
        logger.info(f"statement_kind = {statement_kind} ")
        formatted_code: str = self.get_formatted_code(
            code, self.kafka_topic, self.kafka_broker_url
        )
        logger.info(f"formatted_code = {formatted_code} ")
        if statement_kind not in VALID_STATEMENT_KINDS:
            raise ValueError(
                f"{statement_kind} is not a valid statement kind for a SETU server of "
                f"(should be one of {VALID_STATEMENT_KINDS})"
            )
        self.statement = self.client.create_statement(
            self.session_id, formatted_code, statement_kind
        )
        intervals = polling_intervals([1, 2, 3, 5], 10)
        while waiting_for_output(self.statement):
            logger.info(
                " Setu statement progress {} : {}".format(
                    self.statement.statement_id, self.statement.progress
                )
            )
            time.sleep(next(intervals))
            self.statement = self.client.get_statement(
                self.statement.session_id, self.statement.statement_id
            )
        if self.statement.output is None:
            logger.error(f" Setu Statement {self.statement.statement_id} had no output ")
            raise dbt.exceptions.DbtRuntimeError(
                f"Setu Statement {self.statement.statement_id} had no output"
            )
        logger.info(
            "Setu Statement {} state is : {}".format(
                self.statement.statement_id, self.statement.state
            )
        )
        self.statement.output.raise_for_status()
        if not self.statement.output.execution_success:
            logger.error(
                "Setu Statement {} output Error : {}".format(
                    self.statement.statement_id, self.statement.output
                )
            )
            raise dbt.exceptions.DbtRuntimeError(
                f"Error during Setu Statement {self.statement.statement_id} execution : {self.statement.output.error}"
            )
        return self.statement.output

    def close(self):
        if self.statement is not None and self.statement.state in [
            StatementState.WAITING,
            StatementState.RUNNING,
        ]:
            try:
                logger.info("closing Setu Statement id : {} ".format(self.statement.statement_id))
                self.client.cancel_statement(
                    self.statement.session_id, self.statement.statement_id
                )
                logger.info("Setu Statement closed")
            except Exception as e:
                logger.exception("Setu Statement already closed ", e)

    def fetchall(self):
        if self.statement is not None and self.statement.state in [
            StatementState.WAITING,
            StatementState.RUNNING,
        ]:
            intervals = polling_intervals([1, 2, 3, 5], 10)
            while waiting_for_output(self.statement):
                logger.info(
                    " Setu statement {} progress : {}".format(
                        self.statement.statement_id, self.statement.progress
                    )
                )
                time.sleep(next(intervals))
                self.statement = self.client.get_statement(
                    self.statement.session_id, self.statement.statement_id
                )
            if self.statement.output is None:
                logger.error(f"Setu Statement {self.statement.statement_id} had no output")
                raise dbt.exceptions.DbtRuntimeError(
                    f"Setu Statement {self.statement.statement_id} had no output"
                )
            self.statement.output.raise_for_status()
            if self.statement.output.json is None:
                logger.error(f"Setu statement {self.statement.statement_id} had no JSON output")
                raise dbt.exceptions.DbtRuntimeError(
                    f"Setu statement {self.statement.statement_id} had no JSON output"
                )
            return get_data_from_json_output(self.statement.output.json)
        elif self.statement is not None:
            self.statement.output.raise_for_status()
            return get_data_from_json_output(self.statement.output.json)
        else:
            raise dbt.exceptions.DbtRuntimeError(
                "Setu statement response : {} ".format(self.statement)
            )

    def extract_select_query(self, sql_query):
        """
        Extract SELECT query from DBT query
        """
        import re

        # Regex to match and extract the comment section and everything after 'as'
        match = re.search(r"comment\s+'(.*?)'\s+as\s+(.*)", sql_query, re.DOTALL)
        after_as_text = ""

        if match:
            after_as_text = match.group(2)  # Extract the SQL after 'as'

        # a = "select" + sql_query.split("select")[1]
        return after_as_text.replace("\n", " ")

    def execute_sql_via_pyspark(self, code):
        """
        POC method to push data to kafka via rest API
        """
        file_name = "push_to_kafka.py"
        pyspark_code = self.read_file(file_name)
        pyspark_code = pyspark_code.replace("code_sql", self.extract_select_query(code))

        return pyspark_code

    def read_file(self, file_name):
        with open(file_name, "r") as file:
            file_content = file.read()
        return file_content

    def execute_sql_via_scala(self, code):
        """
        POC method to push data to kafka via spark scala
        """
        file_name = "push_to_kafka.scala"
        scala_code = """
        def createproducer() = {
  import org.apache.kafka.clients.producer.ProducerRecord;

  import com.linkedin.kafka.clients.factory.AvroKafkaConsumerFactory;
  import org.apache.avro.generic.IndexedRecord;
  import org.apache.kafka.clients.consumer.Consumer;
  import com.linkedin.kafka.factory.KafkaClientBuilders;
  import com.codahale.metrics.Meter;
  import com.codahale.metrics.MetricRegistry;
  import com.codahale.metrics.Timer;
  import com.google.common.util.concurrent.RateLimiter;
  import org.apache.avro.generic.GenericArray;
  import org.apache.avro.specific.SpecificData;
  import org.apache.avro.util.Utf8;
  import com.linkedin.avroutil1.compatibility.AvroCompatibilityHelper;
  import com.linkedin.kafka.factory.producer.AvroKafkaProducerCfg;
  import org.apache.avro.generic.IndexedRecord;
  import com.linkedin.kafka.factory.producer.KafkaProducerBuilder;
  import com.linkedin.kafka.linkedinclients.common.LinkedinKafkaClientsSslProperties;

  var sslProperties: LinkedinKafkaClientsSslProperties = null;
  var DEFAULT_TRUSTSTORE_PATH = "/etc/riddler/cacerts";
  var DEFAULT_SECURITY_PROTOCOL = "SSL";
  var DEFAULT_SSL_PROTOCOL = "TLS";
  var DEFAULT_SSL_TRUST_MANAGER_ALGORITHM = "SunX509";
  var DEFAULT_SSL_KEY_MANAGER_ALGORITHM = "SunX509";
  var DEFAULT_SSL_KEY_STORE_TYPE = "pkcs12";
  var DEFAULT_SSL_KEY_STORE_PASSWORD = "work_around_jdk-6879539";
  var DEFAULT_SSL_KEY_PASSWORD = "work_around_jdk-6879539";
  var DEFAULT_SSL_TRUST_STORE_TYPE = "JKS";
  var DEFAULT_SSL_TRUST_STORE_PASSWORD = "changeit";
  var DEFAULT_SSL_SECURE_RANDOM_IMPLEMENTATION = "SHA1PRNG";
  var HADOOP_TOKEN_FILE_LOCATION_KEY = "env.HADOOP_TOKEN_FILE_LOCATION";

  import org.apache.hadoop.security.Credentials
  import org.apache.hadoop.conf.Configuration
  import java.io.{File, IOException}
  import org.apache.hadoop.io.Text;


  def getHadoopCredential(): Credentials = {
    var credentials: Credentials = null
    try {
      // Fetch Credential from local Azkaban executor
      credentials = Credentials.readTokenStorageFile(new File(System.getenv("HADOOP_TOKEN_FILE_LOCATION")), new Configuration())
    } catch {
      case e: Exception =>
        print("Exception when fetching hadoop credentials.", e)
    }
    credentials
  }

  def getSecret(key: Text): Array[Byte] = {
    try {
      val hadoopCredentials = getHadoopCredential()
      val secret = hadoopCredentials.getSecretKey(key)
      if (secret == null || secret.isEmpty) {
        throw new IllegalStateException(s"Could not find secret with key $key")
      }
      secret
    } catch {
      case e: Exception =>
        print("Exception when fetching hadoop credentials.", e)
        null
    }
  }
  import java.nio.charset.StandardCharsets;
  import java.nio.file.Files;
  import java.nio.file.Path;
  import java.util.concurrent.TimeUnit;
  import org.apache.hadoop.io.IOUtils;
  import java.io.ByteArrayInputStream;


  def writeToTempFile(contents: Array[Byte]): File = {
    try {
      // Create a temporary file
      val path: Path = Files.createTempFile(null, null)

      // Write the byte array to the temporary file
      IOUtils.copyBytes(new ByteArrayInputStream(contents), Files.newOutputStream(path), contents.length.toLong, true)

      // Convert the Path to File and ensure it's deleted on exit
      val file: File = path.toFile
      file.deleteOnExit()

      // Check if file was written correctly and set readable permissions
      if (contents.length != file.length() || !file.setReadable(true, true)) {
        throw new IllegalStateException(s"Unable to create or chmod file ${file.getCanonicalPath}")
      }

      // Log the success
      print(s"Created file at ${path.toAbsolutePath} of size ${contents.length} bytes")

      // Return the file
      file
    } catch {
      case e: IOException => throw new IOException("Error writing to temp file", e)
    }
  }


  def getKeystorePath(): String = {
    val keystore = getSecret(new Text("li.datavault.identity"))

    try {
      writeToTempFile(keystore).getCanonicalPath
    } catch {
      case e: IOException =>
        throw new RuntimeException("Could not persist credentials", e)
    }
  }

  import java.io.{ByteArrayInputStream, File, IOException}
  import java.nio.file.{Files, Path}
  import org.apache.hadoop.io.IOUtils

  var _keystoreFile = new File(getKeystorePath())

  def getTruststorePath(): String = {
    val truststore = getSecret(new Text("li.datavault.truststore"))

    // use the default truststore path if a path is not configured in the Credentials
    if (truststore == null) {
      return DEFAULT_TRUSTSTORE_PATH
    }

    try {
      writeToTempFile(truststore).getCanonicalPath
    } catch {
      case e: IOException =>
        throw new RuntimeException("Could not persist the truststore", e)
    }
  }

  def getKeyStorePassword(): String = {
    new String(getSecret(new Text("li.datavault.identity.keystore.password")), StandardCharsets.UTF_8)
  }

  def getKeyPassword(): String = {
    new String(getSecret(new Text("li.datavault.identity.key.password")), StandardCharsets.UTF_8);
  }


  sslProperties = LinkedinKafkaClientsSslProperties.defaults();
  sslProperties.setSslKeyStoreLocation(_keystoreFile.getCanonicalPath());
  sslProperties.setSslTrustStoreLocation(getTruststorePath());
  sslProperties.setSslProtocol(DEFAULT_SSL_PROTOCOL);
  sslProperties.setSslTrustManagerAlgorithm(DEFAULT_SSL_TRUST_MANAGER_ALGORITHM);
  sslProperties.setSslKeyManagerAlgorithm(DEFAULT_SSL_KEY_MANAGER_ALGORITHM);
  sslProperties.setSslKeyStoreType(DEFAULT_SSL_KEY_STORE_TYPE);
  sslProperties.setSslKeyStorePassword(getKeyStorePassword());
  sslProperties.setSslKeyPassword(getKeyPassword());
  sslProperties.setSslTrustStoreType(DEFAULT_SSL_TRUST_STORE_TYPE);
  sslProperties.setSslTrustStorePassword(DEFAULT_SSL_TRUST_STORE_PASSWORD);
  sslProperties.setSslSecureRandomImplementation(DEFAULT_SSL_SECURE_RANDOM_IMPLEMENTATION);

  val cfg = new AvroKafkaProducerCfg()
  cfg._schemaRegistryRestUrl = "http://1.schemaregistry.corp-lva1.atd.corp.linkedin.com:10252/schemaRegistry/api/v2/name/PySparkTestTopicProd/latest"
  cfg._bootstrapServers = "kafka.tracking.kafka.prod-ltx1.atd.prod.linkedin.com:16637"
  cfg._requestTimeoutMs = 100
  cfg._requestRetries = 2
  cfg._retryBackoffMs = 100
  cfg._requestRequiredAcks = "all"
  cfg._scopePath = "all"

  @transient lazy val _producer_builder: KafkaProducerBuilder[String, IndexedRecord] = KafkaClientBuilders.avroProducer(
    "hadoop", // environment name
    "indbt tracking poc", // service name
    "test",
    cfg,
    sslProperties
  )
  var _producer = _producer_builder.build()
  _producer
}

val data = spark.sql("code_sql")

import org.apache.spark.sql.{SparkSession, Row}
import org.apache.avro.Schema
// Create an ObjectMapper instance
import java.net.{HttpURLConnection, URL}

def getJsonResponse(urlStr: String) = {
  import scala.io.Source
  // Create a URL object
  val url = new URL(urlStr)

  // Open a connection to the URL
  val connection = url.openConnection().asInstanceOf[HttpURLConnection]

  try {
    // Set the request method to GET
    connection.setRequestMethod("GET")

    // Get the input stream and read the response
    val inputStream = connection.getInputStream
    val content = Source.fromInputStream(inputStream).mkString
    inputStream.close()

    content

  } finally {
    connection.disconnect()
  }
}

import com.fasterxml.jackson.databind.{JsonNode, ObjectMapper}

val mapper = new ObjectMapper()
val jsonResponse = getJsonResponse("http://1.schemaregistry.corp-lva1.atd.corp.linkedin.com:10252/schemaRegistry/api/v2/name/T3SearchDBTPOC/latest")
val jsonNode: JsonNode = mapper.readTree(jsonResponse)
var n_schemaString = jsonNode.get("schema").asText()
var n_schema = new Schema.Parser().parse(n_schemaString)

data.foreachPartition { (partition: Iterator[Row]) =>
  val _producer = createproducer()
  partition.foreach { row =>
    val startTime = System.currentTimeMillis()
    import org.apache.avro.Schema
    import org.apache.avro.generic.GenericData
    import org.apache.avro.generic.IndexedRecord
    import org.apache.kafka.clients.producer.ProducerRecord;
    import org.apache.spark.sql.{SparkSession, Row}

    import org.apache.avro.generic.GenericData
    import org.apache.avro.generic.IndexedRecord
    import java.nio.ByteBuffer
    import java.util.UUID


    val uuidBytes = ByteBuffer.wrap(java.util.UUID.randomUUID().toString.replace("-", "").getBytes()).array()
    import spark.implicits._

    def rowToIndexedRecord(row: Row): IndexedRecord = {
      import org.apache.avro.generic.{GenericData, IndexedRecord}
      import org.apache.avro.Schema
      import org.apache.spark.sql.Row
      import scala.collection.JavaConverters._
      def convertRowToGenericRecord(row: Row, schema: Schema): IndexedRecord = {
        val record = new GenericData.Record(schema)

        schema.getFields.asScala.foreach { field =>
          val fieldName = field.name()
          val fieldSchema = field.schema()

          if (!row.isNullAt(row.fieldIndex(fieldName))) {
            val value = row.get(row.fieldIndex(fieldName))
            record.put(field.pos(), convertValueToAvro(value, fieldSchema))
          }
        }

        record
      }

      def convertValueToAvro(value: Any, schema: Schema): Any = {
        if (value == null) {
          // Check if the schema allows null values (union with null or nullable field)
          if (schema.getType == Schema.Type.UNION) {
            // Check if one of the union types is NULL
            val nullableType = schema.getTypes.asScala.find(_.getType == Schema.Type.NULL)
            if (nullableType.isDefined) {
              return null
            } else {
              throw new IllegalArgumentException(s"Null value is not allowed for non-nullable field with schema: $schema")
            }
          } else {
            throw new IllegalArgumentException(s"Null value is not allowed for non-nullable field with schema: $schema")
          }
        }

        // Handle non-null values
        schema.getType match {
          case Schema.Type.INT => value.asInstanceOf[Int]
          case Schema.Type.LONG => value.asInstanceOf[Long]
          case Schema.Type.STRING => value.asInstanceOf[String]
          case Schema.Type.BOOLEAN => value.asInstanceOf[Boolean]
          case Schema.Type.BYTES => value.asInstanceOf[Array[Byte]]
          case Schema.Type.FIXED =>
            val byteValue = value match {
              case bytes: Array[Byte] => bytes
              case _ => throw new IllegalArgumentException(s"Expected byte array for fixed, got: ${value.getClass}")
            }
            if (byteValue.length != schema.getFixedSize) {
              throw new IllegalArgumentException(s"Invalid size for fixed type: expected ${schema.getFixedSize}, got ${byteValue.length}")
            }
            new GenericData.Fixed(schema, byteValue)
          case Schema.Type.ENUM =>
            // Ensure the value is one of the allowed symbols
            val enumSymbol = value match {
              case str: String if schema.getEnumSymbols.contains(str) => str
              case _ => throw new IllegalArgumentException(s"Invalid value for enum: $value. Allowed symbols: ${schema.getEnumSymbols}")
            }
            new GenericData.EnumSymbol(schema, enumSymbol)
          case Schema.Type.ARRAY =>
            val elementSchema = schema.getElementType
            value.asInstanceOf[Seq[_]].map(v => convertValueToAvro(v, elementSchema)).asJava
          case Schema.Type.MAP =>
            val valueSchema = schema.getValueType
            value.asInstanceOf[Map[String, Any]].map {
              case (k, v) => k -> convertValueToAvro(v, valueSchema)
            }.asJava
          case Schema.Type.RECORD =>
            val rowValue = value.asInstanceOf[Row]
            convertRowToGenericRecord(rowValue, schema)
          case Schema.Type.UNION =>
            // Handle union types (nullable fields)
            val nonNullSchema = schema.getTypes.asScala.find(_.getType != Schema.Type.NULL).get
            convertValueToAvro(value, nonNullSchema)

          // Add handling for DOUBLE type
          case Schema.Type.DOUBLE => value.asInstanceOf[Double]

          case _ =>
            throw new IllegalArgumentException(s"Unsupported Avro schema type: ${schema.getType}")
        }
      }

      var record = convertRowToGenericRecord(row, n_schema)


      println(record)
      record.asInstanceOf[IndexedRecord]
    }

    val indexedRecord: IndexedRecord = rowToIndexedRecord(row)
    val record = new ProducerRecord[String, IndexedRecord]("test_new_topic", UUID.randomUUID().toString, indexedRecord)

    _producer.send(record)
    val endTime = System.currentTimeMillis()
    val duration = endTime - startTime
    println(s"Record with key sent in $duration ms")
  }
  _producer.flush()
  _producer.close()
}
"""
        scala_code = scala_code.replace("code_sql", self.extract_select_query(code))
        scala_code = scala_code.replace("test_new_topic", self.kafka_topic)
        scala_code = scala_code.replace("PySparkTestTopicProd", self.kafka_topic)
        scala_code = scala_code.replace("T3SearchDBTPOC", self.kafka_topic)
        scala_code = scala_code.replace(
            "kafka.tracking.kafka.prod-ltx1.atd.prod.linkedin.com:16637",
            self.kafka_broker_url,
        )

        return scala_code

    def get_formatted_code(self, code: str, kafka_topic=None, kafka_broker_url=None) -> str:
        # TODO: Handle it in a more generic manner, this is only for POC
        if kafka_topic is not None and kafka_broker_url is not None and "create table" in code:
            # return self.execute_sql_via_pyspark(code) # This method was added to execute Kafka rest API via pyspark
            return self.execute_sql_via_scala(code)
        code_lines = []
        for line in code.splitlines():
            line = line.strip()
            # Ignore depends_on statements in model files
            if not line or line.startswith("-- depends_on:"):
                continue
            """
            StatementKind inference logic (sql/scala/pyspark)
            If Macro sql contains $$spark$$ in the beginning of the line, then spark
            Else If Macro sql contains $$pyspark$$ in the beginning of the line, then pyspark
            Else sql
            """
            if line.startswith("$$" + StatementKind.SPARK.value + "$$"):
                line = line.replace("$$" + StatementKind.SPARK.value + "$$", " ", 1)
            elif line.startswith("$$" + StatementKind.PYSPARK.value + "$$"):
                line = line.replace("$$" + StatementKind.PYSPARK.value + "$$", " ", 1)
            code_lines.append(" " + line)
        formatted_code = os.linesep.join([s for s in code_lines if s.strip()])
        return formatted_code

    def get_statement_kind(
        self,
        code: str,
        kafka_topic: Optional[str] = None,
        kafka_broker_url: Optional[str] = None,
    ) -> StatementKind:
        # TODO: Make it more generic
        if kafka_topic is not None and kafka_broker_url is not None and "create table" in code:
            # For Kafka REST API's this would have been pyspark
            return StatementKind.SPARK

        for line in code.splitlines():
            line = line.strip()
            # Ignore depends_on statements in model files
            if not line or line.startswith("-- depends_on:"):
                continue
            """
            StatementKind inference logic (sql/scala/pyspark)
            If Macro sql contains $$spark$$ in the beginning of the line, then spark
            Else If Macro sql contains $$pyspark$$ in the beginning of the line, then pyspark
            Else sql
            """
            if line.startswith("$$" + StatementKind.SPARK.value + "$$"):
                return StatementKind.SPARK
            elif line.startswith("$$" + StatementKind.PYSPARK.value + "$$"):
                return StatementKind.PYSPARK
            else:
                return StatementKind.SQL

        return StatementKind.SQL
