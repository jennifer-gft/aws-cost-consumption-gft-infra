#!/bin/bash
eventsource=arn:aws:sqs:eu-west-2:484165963982:dev-report-delivery-queue
aws lambda create-event-source-mapping --function-name client-report-storage-master --batch-size 1 --maximum-batching-window-in-seconds 300 --event-source-arn $eventsource

if [ $? -eq 0 ]
then
    echo "Success. The event source trigger was triggered successfully"
else
    echo "Failure. The event source trigger was not successful"
fi
