import os
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

from modules import get_defaultairflow_args, extract_data, transform_data, load_data

with DAG(
    dag_id="spotify_etl",
    default_args=get_defaultairflow_args(),
    description="Statistics of your Spotify account",
    schedule_interval="@once",
    catchup=False,
) as dag:

    args = [f"{datetime.now().strftime('%Y-%m-%d %H')}", os.getcwd()]

    # Tasks
    # 1. Extraction
    task_extract = PythonOperator(
        task_id="extract_data",
        python_callable=extract_data,
        op_args=args,
    )

    # 2. Transformation
    task_transform = PythonOperator(
        task_id="transform_data",
        python_callable=transform_data,
        op_args=args,
    )

    # 3. Loading
    task_load_data = PythonOperator(
        task_id="load_data",
        python_callable=load_data,
        op_args=args,
    )

    # Task dependencies
    task_extract >> task_transform >> task_load_data