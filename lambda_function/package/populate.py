import os
import boto3
import psycopg2
import logging
import logging.handlers


import psycopg2
import sys
import boto3
import os

logging.basicConfig(filename="logname",
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

ENDPOINT="mydb1.crwrwfmegyrd.eu-west-2.rds.amazonaws.com"
PORT="5432"
USER="mydb1"#gftadmin
REGION="eu-west-2"
DBNAME="mydb1" #gftclientdb
PASS="foo12345678"
              
            

def create_table():
    ssm_client = boto3.client('ssm')

    logger = logging.getLogger('INIT-DB')
    logger.setLevel(logging.INFO)
    with psycopg2.connect(f"host={ENDPOINT} dbname={DBNAME} user={USER} password={PASS} ") as conn:
            with conn.cursor() as cur:        
                cur.execute("""CREATE TABLE IF NOT EXISTS customers (
                            client_id int,
                            client_name varchar(255),
                            project varchar(255),
                            environment varchar(255),
                            total_aws_accounts int,
                            descriptions varchar(255),
                            PRIMARY KEY(client_id)
                        );
                        
                        CREATE TABLE IF NOT EXISTS customer_forecast (
                            client_id int NOT NULL,
                            client_name varchar(255),
                            project varchar(255),
                            environment varchar(255),
                            total_aws_accounts int,
                            descriptions varchar(255)
                            
                        );

                        CREATE TABLE IF NOT EXISTS services_gft (
                            client_id int NOT NULL,
                            aws_service varchar(255),
                            time_period_start date,
                            time_period_end date,
                            value varchar(255),
                            comments varchar(255)
                        );

                        CREATE TABLE IF NOT EXISTS todd (
                            client_id int NOT NULL,
                            aws_service varchar(255),
                            time_period_start date,
                            time_period_end date,
                            value varchar(255),
                            comments varchar(255)
                        );
                        
                        """)
                        


    # sql_insert_values = """
    #     INSERT INTO customers (client_name) VALUES ("Hello World");
    # """
        
#gets the credentials from .aws/credentials
session = boto3.Session()
client = session.client('rds')

try:
    conn = psycopg2.connect(host=ENDPOINT, port=PORT, database=DBNAME, user=USER, password=PASS, sslrootcert="SSLCERTIFICATE")
    cur = conn.cursor()
    cur.execute("""SELECT now()""")
    create_table()
    query_results = cur.fetchall()
    print(query_results)
except Exception as e:
    print("Database connection failed due to {}".format(e))  