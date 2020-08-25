'''
    This is test dag for ex7.
    It download data from excel file to vertica DB.
'''
from test_download_data.test_download_data import DownloadData
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
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
    dag_id='test_ex_7v1',
    default_args=default_args,
    schedule_interval=None)

var = Variable.get('test_Variables')


# def get_connection_task():
#     DownloadData.get_connection()


def check_var_task():
    DownloadData.check_var(var)


def check_column_task():
    DownloadData.check_column(var)


def download_to_vertica_task():
    DownloadData.download_to_vertica(var)


def close_connection_task():
    DownloadData.close_connection()


with dag:
    # task0_get_connection = PythonOperator(
    #     task_id='task0_get_connection',
    #     python_callable=get_connection_task)

    task1_download_data = PythonOperator(
        task_id='task_download_data',
        python_callable=check_var_task)

    task2_check_column = PythonOperator(
        task_id='task_check_column',
        python_callable=check_column_task)

    task3_download_to_vertica = PythonOperator(
        task_id='task_download_to_vertica',
        python_callable=download_to_vertica_task)

    task4_close_connection = PythonOperator(
        task_id='task_close_connection',
        python_callable=close_connection_task)

    task1_download_data >> task2_check_column >> task3_download_to_vertica >> task4_close_connection
