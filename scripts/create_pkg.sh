#!/bin/bash

<<<<<<< HEAD
cd ../lambda_function
=======
cd $path_cwd/lambda_function
>>>>>>> 993ad9568addf2249f70950c879e5e55672da12f

chmod +x requirements.txt

FILE=requirements.txt

if [ -f "$FILE" ]; then
<<<<<<< HEAD
  echo "Installing dependencies..."
  echo "From: requirement.txt file exists..."
  pip3 install --target ./package -r "$FILE"
=======
  echo "Installing dependencies for infra..."
  echo "From: requirement.txt file exists..."
  pip3 install -U --target . -r "$FILE"
>>>>>>> 993ad9568addf2249f70950c879e5e55672da12f

else
  echo "Error: requirements.txt does not exist!"
fi
<<<<<<< HEAD
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
=======


>>>>>>> 993ad9568addf2249f70950c879e5e55672da12f
