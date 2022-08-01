
import boto3
import json
import psycopg2



def lambda_handler(event, context):
    event_json=event['Records'][0]['body']
    res=json.loads(event_json)
    print(res['report_type'])

    
    if res['report_type'] == "usage":
        results=res['ResultsByTime']
        for record in results:
           print(record)
           print(record['TimePeriod']['Start'])
           time_period_start=record['TimePeriod']['Start']
           time_period_end=record['TimePeriod']['End']
           resource_list=[]
           cost=0
           for resources in record['Groups']:
               resource_list.append(resources['Keys'][0])
               cost=cost+float(resources['Metrics']['BlendedCost']['Amount'])
           aws_service = ','.join(resource_list)
           value = round(cost, 2)
           print(aws_service)
           print(value)
    elif res['report_type'] == "forecast":
        print("Trying forecast")
    else:
        print("Invalid report type")
      
    try:
        connection = psycopg2.connect(user="gftadmin",
                                  password="testtttttt",
                                  host="gftclientdb.c7pd8q3l1nhp.eu-west-2.rds.amazonaws.com",
                                  port="5432",
                                  database="gftclientdb")
        print(connection)
        cursor = connection.cursor()
        postgres_insert_query = """ SELECT table_schema,table_name FROM information_schema.tables """
        cursor.execute(postgres_insert_query)
        version = cursor.fetchone()[0]
        print(version)
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into mobile table", error)
    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


   
 