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
        scala_code = self.read_file(
            os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
        )
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
