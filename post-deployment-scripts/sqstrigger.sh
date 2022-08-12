#!/bin/bash
aws lambda create-event-source-mapping --function-name client-report-storage-master --batch-size 1 --maximum-batching-window-in-seconds 300 --event-source-arn arn:aws:sqs:eu-west-2:484165963982:dev-report-delivery-queue
