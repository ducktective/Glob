import vertica_python
import numpy as np
import pandas as pd
import xlrd
import re
from airflow.hooks.base_hook import BaseHook


class DownLoadData:
    # Config for connection
    connection = BaseHook.get_connection('Vertica_connection')
    # Check ui Airflow in browser for details
    connection_info = {'host': connection.host,
                       'port': 5433,
                       'user':  connection.user,
                       'password':  connection.password,
                       'database':  connection.db}

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

    # decorator for static method. It's unnecessary

    @staticmethod
    def check_dir(dir_to_file):
        '''
            Check for directory and file existing.
        '''
        dir_name = re.match(r'.*/', dir_to_file).group(0)
        if os.path.isdir(dir_name) == False:
            logging.warning('This directory doesn\'t exist')
            raise AirflowSkipException()
        elif os.path.islfile(dir_to_file) == False:
            logging.warning('This file doesn\'t exist')
            raise AirflowSkipException()
        else:
            Variable.set('Variables_ready_for_load', str(dir_to_file))

    @staticmethod
    def chech_columns(file_):
        df = pd.read_csv(file_)
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
    def download_data(file_):
        with vertica_python.connect(**connection_info) as conn:
            # do things
            cur = conn.cursor()
            if chech_columns(file_) == True:
                csv_file = convert_to_csv(file_)
                cur.execute(
                    fr"COPY test_vert.STG_NEW_CAPACITIES(commodity,cause,region,country_or_teritory,company,site,plant_no,estimated_start_date,exp_ann_cap_change,total_annual, swing_capable) FROM local {csv_file} PARSER fcsvparser() ABORT ON ERROR;")
