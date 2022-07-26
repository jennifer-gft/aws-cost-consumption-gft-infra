import json
import boto3
import logging
import sys
from botocore.exceptions import ClientError
import datetime
from dateutil.relativedelta import relativedelta

logger = logging.getLogger(__name__)


def lambda_handler(event, context):


    
    return {
        'statusCode': 200,
    }