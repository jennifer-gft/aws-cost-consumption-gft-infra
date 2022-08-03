#!/bin/bash

cd /Users/e-tehy/Documents/awsTraining/aws-cost-consumption-gft-infra/lambda_function

chmod +x requirements.txt

FILE=requirements.txt

if [ -f "$FILE" ]; then
  echo "Installing dependencies..."
  echo "From: requirement.txt file exists..."
  pip3 install --target ./package -r "$FILE"

else
  echo "Error: requirements.txt does not exist!"
fi

FILE=populate.py

if [ -f "$FILE" ]; then
  echo "Running Python Populate..."
  echo "From: requirement.txt file exists..."
  pip3 install --target ./package -r "$FILE"

else
  echo "Error: requirements.txt does not exist!"
fi
