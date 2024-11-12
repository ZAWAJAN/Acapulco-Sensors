# Software Guide for Cube Illuminance meter

Now that you have the assembled device ready, you can collect the data from it. There are numerous ways, the data can be collected once, when needed, or it could be a chronological setup, for example using 'cron'.
The code to be used is pretty much the same as the one used during calibration.

Remember to apply the adjustments figured out during the calibration process. That needs to be done by hardcoding it into the provided [python script](src/code/sensor_data_collect_store_csv.py).

# Usage Instructions

You can run the python script directly from the command line, providing a name of the csv file to store the data in, like so:
```bash
python3 sensor_data_collect_store_csv.py "Data_Log_File.csv"
```
Or you could use the [bash script](src/code/run_sensor_collector.sh), which automatically creates a folder named with this days timestamp. In the bash script, at the beginning you can specify the desired directory.
```bash
bash run_sensor_collector.sh
```

The sensor is meant to collect data periodically. To set this up, we refer you to [this example guide on cron](https://phoenixnap.com/kb/set-up-cron-job-linux).