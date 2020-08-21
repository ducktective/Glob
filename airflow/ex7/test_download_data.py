'''
This script downloading data in to vertica.
'''

import vertica_python
import numpy as np
import pandas as pd
import xlrd
import re
import os
from airflow.exceptions import AirflowSkipException
from airflow.exceptions import AirflowException
import logging

# next line for connection to vertica
from airflow.hooks.base_hook import BaseHook
import shutil


class DownloadData():

    @staticmethod
    def check_var(var_value):
        '''
            var_value is 
            Check for directory and file on existing.
        '''
        dir_name = re.match(r'.*/', var_value).group(0)
        if os.path.isdir(dir_name) == False:
            logging.warning('This directory doesn\'t exist')
            raise AirflowSkipException()
        elif os.path.isfile(var_value) == False:
            logging.warning('This file doesn\'t exist')
            raise AirflowSkipException()

    @staticmethod
    def check_column(file_):
        '''
        Take file in file_ variable.
        '''
        df = pd.read_excel(file_)
        column_tuple = ('Commodity', 'Cause', 'Region',
                        'Country / Territory', 'Company',
                        'Site', 'Plant No.', 'Estimated Start Date',
                        'Expected Annual Capacity Change (kt)',
                        'Total Annual Capacity (kt)', 'Swing Capable')
        for column in column_tuple:
            if column not in df.columns:
                logging.error(f'Dataframe {file_} didn\'t pass validation.')
                del df
                raise AirflowException()
                return False
        logging.info(f'Dataframe {file_} pass validation.')
        del df
        return True

    @staticmethod
    def convert_to_csv(file_):
        '''
        Take excel file whith data. Then transform in on csv format and download this in vertica.
        '''
        df = pd.read_excel(file_)
        dir_name = re.match(r'.*/', file_).group(0)
        new_csv_file = os.path.join(dir_name, 'NEW_CAPACITIES.csv')
        df.to_csv(new_csv_file, index=False)
        del df
        return new_csv_file

    @staticmethod
    def download_to_vertica(file_):
        csv_file = DownloadData.convert_to_csv(file_)
        connection = BaseHook.get_connection(
            'Test_bad_Vertica_connection')
        connection_info = {'host': connection.host,
                           'port': 5433,
                           'user':  connection.login,
                           'password':  connection.password,
                           'database':  connection.schema}
        with vertica_python.connect(**connection_info) as conn:
            logging.info('1')
            cur = conn.cursor()
            logging.info('2')
            cur.execute(
                fr"COPY test_vert.STG_NEW_CAPACITIES(commodity,cause,region,country_or_teritory,company,site,plant_no,estimated_start_date,exp_ann_cap_change,total_annual, swing_capable) FROM local '{csv_file}' PARSER fcsvparser() ABORT ON ERROR;COMMIT;")
            logging.info('3')
            loaded_data = os.path.join(
                '/usr', 'local', 'airflow', 'data', 'test_loaded_data')
            shutil.copyfile(csv_file, loaded_data)
            logging.info('4')
