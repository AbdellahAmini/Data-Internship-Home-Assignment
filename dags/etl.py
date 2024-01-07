from airflow import DAG
from datetime import timedelta, datetime

from airflow.decorators import dag, task
from airflow.providers.sqlite.hooks.sqlite import SqliteHook
from airflow.providers.sqlite.operators.sqlite import SqliteOperator

from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data
from src.queries import TABLES_CREATION_QUERIES

@task(task_id="extract_data")
def extract():
    """Extract data from jobs.csv."""
    extract_data()

@task(task_id="transform_data")
def transform():
    """Clean and convert extracted elements to json."""
    transform_data()

@task(task_id="load_data")
def load():
    """Load data to sqlite database."""
    sqlite_hook = SqliteHook(sqlite_conn_id="sqlite_default")
    load_data(sqlite_hook)

DAG_DEFAULT_ARGS = {
    "depends_on_past": False,
    "retries": 3,
    "retry_delay": timedelta(minutes=15)
}

@dag(
    dag_id="etl_dag",
    description="ETL LinkedIn job posts",
    tags=["etl"],
    schedule="@daily",
    start_date=datetime(2024, 1, 7,21,10),
    catchup=False,
    default_args=DAG_DEFAULT_ARGS
)
def etl_dag():
    """ETL pipeline"""

    create_tables = SqliteOperator(
        task_id="create_tables",
        sqlite_conn_id="sqlite_default",
        sql=TABLES_CREATION_QUERIES
    )

    create_tables >> extract() >> transform() >> load()

etl_dag()
