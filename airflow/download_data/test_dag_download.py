'''
    This is test dag for ex7.
    It download data from excel file to vertica DB.
'''
import download_data
from airflow import DAG
from airflow.exceptions import AirflowSkipException
from airflow.exceptions import AirflowException
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import logging
import os
from airflow.models import Variable
# this line for connection
from airflow.models.connection import Connection

# setting for DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2020, 8, 10),
}

# i haven't schedual for this ex.
dag = DAG(
    dag_id='test_ex_7',
    default_args=default_args,
    schedule_interval=None)



logging.basicConfig(level=logging.INFO)


def download_task():
    file = os.path.join('/usr','local','airflow','libs','NEW_CAPACITIES.xlsx')
    download_data.DownLoadData.download_data(file)


with dag:
    task_download_data = PythonOperator(
        task_id='task_download_data',
        python_callable=download_task)
