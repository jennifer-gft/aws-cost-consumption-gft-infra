#!/bin/bash

cd ../lambda_function

chmod +x requirements.txt

FILE=requirements.txt

if [ -f "$FILE" ]; then
  echo "Installing dependencies..."
  echo "From: requirement.txt file exists..."
  pip3 install --target ./package -r "$FILE"

else
  echo "Error: requirements.txt does not exist!"
fi
cd package/
FILE=populate.py

if [ -f "$FILE" ]; then
  echo "From: populate.py file exists..."
  echo "changing directory to package"

  echo "Running Python Script..."
  python3 populate.py

else
  echo "Error: populate.py does not exist!"
fi
