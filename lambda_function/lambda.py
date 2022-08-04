
import boto3
import json
import psycopg2



def lambda_handler(event, context):
    event_json=event['Records'][0]['body']
    res=json.loads(event_json)
    print(res['report_type'])
    client_name = res["client_name"]
    project = res["project_name"]
    description = res["description"]
    environment = res["client_env"]
    total_aws_accounts = res["total_env"]
    try:
        connection = psycopg2.connect(user="gftadmin",
                                  password="foo12345678",
                                  host="gftclientdb.c7pd8q3l1nhp.eu-west-2.rds.amazonaws.com",
                                  port="5432",
                                  database="gftclientdb")
        print(connection)
        cursor = connection.cursor()

        cursor.execute("SELECT client_id from public.customer WHERE client_name = %s and project = %s", (client_name, project))

        if cursor.rowcount > 0:
            id_of_row = cursor.fetchone()[0]
        else:
            cursor.execute("INSERT INTO public.customer ( client_name, project, environment, total_aws_accounts, description) VALUES (%s,%s,%s,%s,%s) ON CONFLICT ON CONSTRAINT customer_un DO NOTHING",(client_name, project, environment, total_aws_accounts, description))
            id_of_row = cursor.fetchone()[0]        
        print("Customer id => ",id_of_row)
        #id_of_row = cursor.fetchone()[0]
        #count = cursor.rowcount
        #print(id_of_row, "Customer record inserted successfully into table")
    
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
               cursor.execute("INSERT INTO public.services (client_id, aws_services, time_period_start, time_period_end, value, additional_comments) VALUES (%s, %s, %s, %s, %s, %s)",(id_of_row, aws_service, time_period_start, time_period_end, value, "Test"))
            
            print("Account usage details stored successfully for client ",client_name)
            
        elif res['report_type'] == "forecast":
            print("Trying forecast")
            results=res['ForecastResultsByTime']
            for record in results:
                print(record)
                forecast_period_start=record['TimePeriod']['Start']
                forecast_period_end=record['TimePeriod']['End']
                amount=round(float(record['MeanValue']), 2)
                if int(total_aws_accounts) > 1:
                    comments= "Amount times "+ total_aws_accounts + " accounts"
                    print(comments)
                cursor.execute("INSERT INTO public.forecast (client_id, time_period_start, time_period_end, amount, additional_comments) VALUES(%s,%s,%s,%s,%s)",(id_of_row, forecast_period_start,forecast_period_end,amount,comments))
            
            print("Forecast stored successfully for client ",client_name)

        else:
            print("Invalid report type")
            
   
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into database table, ", error)
        
    finally:
        # closing database connection.
        if connection:
            connection.commit()
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
  