import json
import boto3
import logging
import sys
from botocore.exceptions import ClientError
import datetime
from dateutil.relativedelta import relativedelta

logger = logging.getLogger(__name__)


def send_queue_message(message):
    # Get the service resource
    sqs = boto3.resource('sqs')
    
    # Get the queue
    queue = sqs.get_queue_by_name(QueueName='dev-report-delivery-queue')
    
    # Create a new message
    response = queue.send_message(MessageBody=message)
    print(response.get('MessageId'))




def lambda_handler(event, context):
    client = boto3.client('ce',region_name='eu-west-2')
    start = datetime.date.today() - relativedelta(months=3)
    end = datetime.date.today() 
    print(start)
    CAUMsg = client.get_cost_and_usage(
        TimePeriod={
            'Start': start.isoformat(),
            'End' : end.isoformat()
        },
        Granularity='MONTHLY',
        Metrics = ["BlendedCost"],
        GroupBy = [
        {
            'Type': 'DIMENSION',
            'Key': 'SERVICE'
        },
        {
            'Type': 'TAG',
            'Key': 'Name'
        }
    ]
    )
    # TODO implement
    
    send_queue_message(json.dumps(CAUMsg))
    
    return {
        'statusCode': 200,
        'body': json.dumps(CAUMsg)
    }