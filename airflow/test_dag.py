'''
This is test dag. BAD.
'''

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import logging
import os
# That row for variables
from airflow.models import Variable

# It is default arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2020, 8, 10),
}

logging.basicConfig(filename='custome_log_file.log', level=logging.INFO)

dag = DAG(
    dag_id='test_ex_6',
    default_args=default_args,
    schedule_interval='0 18 * * mon')


def print_var_value_in_log(name):
    custome_log_file = os.path.join(
        'us', 'local', 'airflow', 'libs2', 'log.log')
    logging.info(f'{name}\'s Value = {Variable.get(name)}')


def check_data_path(data_path_name):
    data_path = Variable.get(data_path_name)
    if data_path:
        logging.warning('No data available.')
        raise AirflowSkipException()
    elif os.path.isdir(data_path):
        logging.warning('This directory doesn\'t exist.')
        raise AirflowSkipException()
    else:
        logging.info('data_parh is correct.')


def check_table_name(table_name):
    table_name = Variable.get(table_name)
    if table_name:
        logging.warning('No value in table_name')
        raise AirflowException()
    elif table_name != 'REUTERS':
        logging.error(f'table_name = {table_name}, but we need \'REUTERS\'')
        raise AirflowException()
    else:
        logging.info('table_name = REUTERS')


def var_ready_for_load(var):
    variable = Variable.get(var)
    variable.ready_for_load = True


with dag:

    task1_log_var_value = PythonOperator(
        task_id='task_print_var_value_in_log',
        python_callable=print_var_value_in_log,
        op_args='TEST_PHRASE')

    task2_data_path = PythonOperator(
        task_id='task_data_path',
        python_callable=check_data_path,
        op_args='data_path')

    task3_table_name = PythonOperator(
        task_id='task_table_name',
        python_callable=check_table_name,
        op_args='table_name')

    task4_ready_for_load = PythonOperator(
        task_id='task4_ready_for_load',
        python_callable=check_table_name,
        op_args='Variables')

    # I don't know about this. Do I realy need this in my case?
    task1_log_var_value >> task2_data_path >> task3_table_name
