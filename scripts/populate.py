import os
import boto3
import psycopg2
import logging

def lambda_handler(event, context):
    ssm_client = boto3.client('ssm')

    logger = logging.getLogger('INIT-DB')
    logger.setLevel(logging.INFO)
    try:
        db_host = os.environ['mydb1.crwrwfmegyrd.eu-west-2.rds.amazonaws.com']
        db_name = os.environ['gftclientdb']
        app_db_user = os.environ['gftadmin']
        app_db_pass = os.environ['foo12345678']
        app_db_name = os.environ['gftclientdb']
        # env = os.environ['ENV']
        # project = os.environ['PROJECT']
        # pg_master_pwd = ssm_client.get_parameter(Name=f'/{project}/{env}/database/master-password',WithDecryption=True)['Parameter']['Value']
        # pg_master_user = ssm_client.get_parameter(Name=f'/{project}/{env}/database/master-user',WithDecryption=True)['Parameter']['Value']
    except:
        return {
            'error': 'UnableToGetEnvInformations'
        }

    # Check if the db exist
    # logger.info('Checking the the db exists...')
    # with psycopg2.connect(f"host={db_host} dbname={db_name} ") as conn:
    #     conn.autocommit = True
    #     with conn.cursor() as cur:
    #         cur.execute(f"SELECT count(*) FROM pg_user where usename = '{app_db_user}';")
    #         if cur.fetchone()[0] == 1:
    #             return {
    #                 'Error': 'UsernameAlreadyCreated'
    #             }

    # logger.info('DB does not exists, creating username and db')
    # try:
    #     with psycopg2.connect(f"host={db_host} dbname={db_name} user={pg_master_user} password={pg_master_pwd} ") as conn:
    #         conn.autocommit = True
    #         with conn.cursor() as cur:
    #             cur.execute(f"CREATE USER {app_db_user} WITH PASSWORD '{app_db_pass}';")
    #             cur.execute(f"CREATE DATABASE {app_db_name};")
    #             cur.execute(f"GRANT ALL PRIVILEGES ON DATABASE {app_db_name} TO {app_db_user}")
    # except Exception as e:
    #     logger.exception(e)
    #     logger.error('Unable to create database')
    #     return {
    #             'Error': 'UnableToCreateDatabase'
    #         }

    # logger.info('Username and db created')
            
    sql_create_table = """
        CREATE TABLE IF NOT EXISTS customers (
            client_id int NOT NULL,
            client_name varchar(255),
            project varchar(255),
            environment varchar(255),
            total_aws_accounts int,
            descriptions varchar(255),
            PRIMARY KEY(client_id)
        );

        CREATE TABLE IF NOT EXISTS customer forecast (
            client_id int NOT NULL,
            time_period_start date,
            time_period_end date,
            value varchar(255),
            comments varchar(255)
        );

        CREATE TABLE IF NOT EXISTS services_gft (
            client_id int NOT NULL,
            aws_service varchar(255)
            time_period_start date,
            time_period_end date,
            value varchar(255),
            comments varchar(255)
        );
    """

    # sql_insert_values = """
    #     INSERT INTO test (name) VALUES ("Hello World");
    # """

    # logger.info('Creating table(s) + populate...')
    # try:
    #     with psycopg2.connect(f"host={db_host} dbname={app_db_name} user={app_db_user} password={app_db_pass} ") as conn:
    #         with conn.cursor() as cur:
    #             cur.execute(sql_create_table)
    #             cur.execute(sql_insert_values)
    #     logger.info('Created tables + populate')
    #     return {
    #         'created': 'true'
    #     }
    # except Exception as e:
    #     logger.exception(e)
    #     logger.error('Unable to create table + populate')
    #     return {
    #         'created': 'false'
    #     } 