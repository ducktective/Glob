import vertica_python
import os

conn_info = {'host': '172.17.0.1',
             'port': 5433,
             'user': 'dbadmin',
             'password': '',
             'database': 'docker'}

# # simple connection, with manual close
# connection = vertica_python.connect(**conn_info)
# # do things
# connection.close()

# using with for auto connection closing after usage
with vertica_python.connect(**conn_info) as conn:
      # do things
      cur = conn.cursor()
      f = os.path.join('/usr', 'local', 'airflow', 'data',
                       'test_variable', 'NEW_CAPACITIES.csv')
      cur.execute(
          fr"COPY test_vert.STG_NEW_CAPACITIES(commodity,cause,region,country_or_teritory,company,site,plant_no,estimated_start_date,exp_ann_cap_change,total_annual, swing_capable) FROM local '{f}' PARSER fcsvparser() ABORT ON ERROR;")
