# Airflow Log Analyzer
This project creates a python script (./inserts/scripts/log-analyzer.py) to read log files (./logs) for dag_id=test_logging_dag.py

## Summary
Environment: Python 3.12
Astronomer, Docker, Airflow


Step 1: Create an astronomer project

Step 2: Run a sample dag "test_logging_dag.py"

Step 3: Verify Airflow UI (screenshots available)

Step 4: Mount airflow logs from docker container to ./logs folder

╰─$ docker volume ls | grep de-sb-airflow-log_

Then Create a temporary container to copy them out:

docker run --rm -v de-sb-airflow-log_bb03b3_airflow_logs:/from -v "$PWD/logs":/to alpine \
  sh -c "cp -r /from/* /to/"

Step 5: Run program "log-analyzer.py" to read these logs and look for phrase "ERROR - "


The screenshots are attached.
