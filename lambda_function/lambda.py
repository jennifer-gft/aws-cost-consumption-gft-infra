
import boto3
import json

def lambda_handler(event, context):
    event_json=event['Records'][0]['body']
    res=json.loads(event_json)
    print(res['report_type'])
    try:
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
           
    except ValueError as e:
        print("dssdsd==>",e)
 