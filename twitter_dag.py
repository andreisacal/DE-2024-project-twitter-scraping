#datetime
from datetime import timedelta
from datetime import datetime
# The DAG object
from airflow import DAG
# Operators
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
# Pull the scraping function from twitter_etl.py
from twitter_etl import run_twitter_etl

# Define default arguments for the Airflow DAG
default_args = {
    "owner": "airflow", # Specifies the owner of the DAG
    "depends_on_past": False, # Determines whether the DAG should depend on the previous run's success or failure
    "start_date": datetime(2024,4,8), # Specifies the start date for the DAG runs
    "email": ["airflow@example.com"], # Provides an email address or a list of email addresses to which notifications should be sent
    "email_on_failure": False, # Determines whether to send an email notification when the DAG run fails
    "email_on_retry": False, # Determines whether to send an email notification when a retry is triggered
    "retries": 1, # Specifies the number of retries that should be attempted in case of a task failure
    "retry_delay": timedelta(minutes=1) # Specifies the delay between retries
}

# Define a new Airflow DAG named "twitter_dag"
dag = DAG(
    "twitter_dag",
    default_args= default_args,
    description= "My first ETL code"
)

# Define a PythonOperator task within the DAG to execute the Twitter ETL process
run_etl = PythonOperator(
    task_id="complete_twitter_etl",
    python_callable=run_twitter_etl, # Python function to be called
    dag=dag
)

run_etl # Add the task to the DAG