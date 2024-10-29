<p align="center">
  <img src="https://raw.githubusercontent.com/dbt-labs/dbt/ec7dee39f793aa4f7dd3dae37282cc87664813e4/etc/dbt-logo-full.svg" alt="dbt logo" width="500"/>
</p>
<p align="center">
  <a href="https://github.com/dbt-labs/dbt-spark/actions/workflows/main.yml">
    <img src="https://github.com/dbt-labs/dbt-spark/actions/workflows/main.yml/badge.svg?event=push" alt="Unit Tests Badge"/>
  </a>
  <a href="https://circleci.com/gh/dbt-labs/dbt-spark/?branch=main">
    <img src="https://circleci.com/gh/dbt-labs/dbt-spark/tree/main.svg?style=shield" alt="Integration Tests Badge"/>
  </a>
</p>

**[dbt](https://www.getdbt.com/)** enables data analysts and engineers to transform their data using the same practices that software engineers use to build applications.

dbt is the T in ELT. Organize, cleanse, denormalize, filter, rename, and pre-aggregate the raw data in your warehouse so that it's ready for analysis.

## in-dbt-spark
The `in-dbt-spark` package contains code to connect with Spark Clusters @ LinkedIn.

We added a new method to the OSS dbt-spark package to connect dbt with cluster-based spark deployments @ LinkedIn (code name Setu).
This new method implementation will leverage in-house **Setu** for the programmatic submission of Spark jobs.


**Setu** provides a narrow waist Spark job submission interface that in turn would allow for the programmatic submission of Spark jobs from anywhere, subject to authentication, while managing multiple Spark versions and clusters under the hood.
Using Setu for DBT will enable users to move much more independently and faster.

## Major Implementation

The Table below represents the mapping of our custom implementation for DB conventions.

| Class                  | DB                   |
|------------------------|----------------------|
| SparkConnectionManager | SQLConnectionManager |
| SetuSession            | DB Connection        |
| SetuSessionHandler     | Connection Handler   |
| SetuStatementCursor    | DB cursor            |

### SparkConnectionManager

This class is responsible for managing the connections like opening, closing and error handling scenarios.

#### 1.  open(cls, connection)

   open() is a classmethod that gets a connection object (which could be in any state, but will have a Credentials object with the attributes you defined above), creates a new SetuSession using SetuSessionManager and moves it to the 'open' state.

   Generally this means doing the following:
   - if the connection is open already, log and return it.
     - create a connection handle using the credentials
         - on success:
             - set connection.state to `'open'`
             - set connection.handle to the handle object
                 - this is what must have a cursor() method that returns a cursor!
         - on error:
             - set connection.state to `'fail'`
             - set connection.handle to `None`
             - raise a dbt.exceptions.FailedToConnectException with the error and any other relevant information

#### 2. cancel(self, connection)
cancel is an instance method that gets a connection object and attempts to cancel any ongoing queries by calling the cancel on the handle object.

#### 3.  exception_handler(self, sql, connection_name='master')
exception_handler is an instance method that returns a context manager that will handle exceptions raised by running queries, catch them, log appropriately, and then raise exceptions dbt knows how to handle.

### SetuSessionHandler
  Equivalent to a DB connection handler, it is responsible for creating and executing cursors. This class creates SetuStatementCursor and executes the cursor with DBT compiled sqls

### SetuSession
This is a spark Interactive session responsible for creating spark context with requested resources from the yarn RM. This class is responsible for managing a remote SETU session and high-level interactions with it.

### SetuStatementCursor
This class is responsible for managing the SETU statements and high-level interactions with it. It takes care of creating, executing, waiting till SETU statement results are available and closing the SETU statement.


## Getting started

- [Install dbt](https://docs.getdbt.com/docs/installation)
- Read the [introduction](https://docs.getdbt.com/docs/introduction/) and [viewpoint](https://docs.getdbt.com/docs/about/viewpoint/)


#### create virtual environment for dbt

```
cd ~
mkdir dbt_env
python3.9 -m venv ~/dbt_env
source ~/dbt_env/bin/activate
```

#### Install DBT Core

```
pip install dbt-core
```

#### Install DBT Spark from Code

```
git clone this repo
cd in-dbt-spark
pip install -r requirements.txt
python setup.py install
```

#### verify installation

```
pip list | grep dbt
# Output:
dbt-core          x.x.x
dbt-extractor     x.x.x
in-dbt-spark      x.x.x
```

## Running locally

**step 1:** Run **dbt init** command to bootstrap dbt project. This step should create a dbt project.

**step 2:** create new folder named profiles and create profiles.yml empty file.

**step 3:** Create new profile in profiles.yml similar to below,

```
dbt_hello_world:
  outputs:
    dev:
      type: spark # connection Type (Spark/Presto/Postgres)
      method: setu  # connection Method (setu/odbc/thrift)
      url: 'https://setu@linkedin.com'
      schema: xxxx  #  schema to persist dbt produced tables
      proxy_user: xxxx  # run spark jobs as proxy user
      queue: xxxx  #  grid queue to submit spark jobs. Defaults to misc_default
      session_name: dbt_hello_world  # unique name for spark session (UUID suffix internally)
      metadata:  # High-level tracking metadata used to provide contextual information about the application
        name: dbt_hello_world
        desciption: hello world project for dbt
        org: xxxx
      spark_conf:  # Additional configs that may be needed for spark app execution (pass-through)
        spark.driver.cores: 1  # Defaults to 2
        spark.executor.cores: 1  # Defaults to 2
        spark.driver.memory: 1G  # Defaults to 4G
        spark.executor.memory: 2G  # Defaults to 8G
      execution_tags:  # Used to determine the target cluster dynamically at runtime.
        gpu: false  # If the spark job requires gpu for processing. Defaults to false
        pool: dev  # Execution environment for the job. Defaults to Dev
      jars: # List of ivy coordinates of the artifacts required by the spark app
        - com.linkedin.xxxx:xxxx:+?transitive=false
```
step 5: Add models and run below commands to compile/test/run

```
# COMPILE:
dbt compile --profiles-dir ./profiles --target dev

# RUN:
dbt run --profiles-dir ./profiles --target dev --threads x

# TEST:
dbt test --profiles-dir ./profiles --target dev --threads x

# GENERATE DOCS:
dbt docs generate --profiles-dir ./profiles --target dev

# SERVE DOCS:
dbt docs serve --profiles-dir ./profiles --port 8080
```

## Reporting bugs and contributing code

- Want to report a bug or request a feature? - Reach out to dbt-dev@linkedin.com
- Want to help us build dbt? Check out the [Contributing Guide](https://github.com/linkedin/in-dbt-spark/blob/HEAD/CONTRIBUTING.md)
