#!/bin/bash

# Get in the proper directory
cd /home/acapulco-rpi-zero/CubeLux/

# Define the CSV file name (this could be dynamically generated, here it's static for example)
CSV_FILE="sensor_data_$(date +'%Y%m%d').csv"

# Run the Python script, passing the CSV file as an argument
python3 sensor_data_collect_store_csv.py "$CSV_FILE"
