from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import logging

def log_something():
    logging.info("This is an INFO log from log_something task.")
    logging.warning("This is a WARNING log from log_something task.")
    logging.error("This is an ERROR log from log_something task.")

def log_another_thing():
    logging.info("Another INFO log from log_another_thing task.")

default_args = {
    'owner': 'airflow',
    'start_date': datetime.utcnow() - timedelta(days=1),
}

with DAG(
    dag_id='test_logging_dag',
    default_args=default_args,
    schedule=None,      # Use 'schedule' instead of 'schedule_interval'
    catchup=False,
    tags=['test'],
) as dag:

    task1 = PythonOperator(
        task_id='log_something',
        python_callable=log_something,
    )

    task2 = PythonOperator(
        task_id='log_another_thing',
        python_callable=log_another_thing,
    )

    task1 >> task2
