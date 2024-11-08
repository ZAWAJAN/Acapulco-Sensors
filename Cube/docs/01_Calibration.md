# Cube Device Sensors calibration

For best results, before you assemble the final cubic device, first the ==Ambient2Click== lux sensors have to be calibrated, as there always might be some small differences between each sensor, that might differ even more from the true readings of proffessional grade meter.

Here we assume you'll have to borrow a proper illuminance meter for the calibration process, like the [Konica Minolta T-10MA](https://www.konicaminolta.eu/eu-en/hardware/measuring-instruments/light-and-display-measurement/illuminance-meters/t-10a-t-10ma), which we used.

The calibration process needs a rather stable environment and light source. We did calibraton in two settings:
1. artificial light in a dark room
2. room with a single window during an overcast day

During callibration, all the sensors have to be as close as possible to each other. For this purpose, a custom laser cut calibration bench can be fabricated using provided [CAD files](../src/hardware/Calibration_Bench.dwg) - see explanation below.

## Hardware Assembly - Calibration Setup

1. **Calibration Bench:**
	- You can find the CAD file for the Calibration Bench [here](../src/hardware/Calibration_Bench.dwg).
	- Laser cut and assemble the calibration bench. refer to the [Instructions](Images/Calibration_Bench_Assembly_Diagram.png) provided. Use glue to stick the sensor brackets to the main board with holes.
	- ![Calibration Bench Assembly Diagram](Images/Calibration_Bench_Assembly_Diagram.png).
	- Place the sensors in the slots on the back of the bench. Number them so you know which one is which. Use tape to keep them in place.
	- There is one additional hole in the centre of the bench face - it can be used either to place the reference meter, or additional sensor to be calibrated (which we did for our purposes).
	- Use a milky skotch tape to cover the holes through which the sensors look outwards.
2. **Wire:**
   - Connect the "Ambient 2 Click" sensors to the TCA9548A multiplexer.
   - The humidity and temperature sensor is not needed in this step, but you can also connect it to the multiplexer
   - Wire the multiplexer to the Raspberry Pi Zero.
   - Follow the [Wiring Diagram](Images/Wiring_Diagram.png)
   - ![Wiring Diagram](Images/Wiring_Diagram.png)
3. **Desk Setup:**
	- Print an angle measuring sheet. This will help you rotate the bench evenly each measurement step.
	- The bench centre should also be in the center of rotation.

## Software

1. **Installation:**
   - The code is proven to work on a Raspberry Pi Bookworm OS.
   - Before anything, update your Raspberry Pi system and libraries:
     ```bash
     sudo apt-get update
	 sudo apt-get upgrade
     ```
	- All the required python libraries (smbus, time, csv, argparse) should be installed by default on a Raspberry Pi system.
2. **Running the Software:**
   - Execute the python script [sensor_data_collect_store_csv.py](../src/code/sensor_data_collect_store_csv.py) to capture readings directly to a .csv file in the same folder:
     ```bash
     # Run the Python script, passing the CSV file as an argument
	 python3 sensor_data_collect_store_csv.py "CSV_FILE.csv"
     ```
   - Or use the bash script [run_sensor_collector.sh](../src/code/run_sensor_collector.sh), in which you have to specify the destination folder. The script will automatically create a new .csv file named with the current day:
     ```bash
     sudo bash run_sensor_collector.sh
     ```
   - Check if the readings make sense and if everything is stored properly. Refer to [Cube_Troubleshooting](04_Cube_TroubleShooting.md) in case problems arise.
3. **Proceed to Calibraation**

## Calibration Steps

1. **Table Setup**
	- Place the light source and the center of the calibration bench on the same height
	- the distance from the light source to the calibration bench shoould be roughly 5 times the diameter of the light source
	- Place the calibration bench on the angular measure centre, so it rotates on the axis of the center (the centre sensor in the middle of the bench)
	- Start with the bench facing the light source.
	- Make sure there are no other visible light sources to minimise the measurement interferance.
2. **Take a measurement**
 	- Run the [run_sensor_collector.sh](../src/code/run_sensor_collector.sh) bash script, which will create the csv file with measurements. Each time you run the script, new measurements will be added as next rows.
	```bash
  	sudo bash run_sensor_collector.sh
	```
 	- As you can see, the measurements are also displayed in the command line, make sure they look correct. For example, it may happen that the first measurement is 0. Then just take another one and it should normalise.
	- Next, take measurements with the reference meter. To be thorough, you should take a measurement for each of the sensors, keeping the measuring piece as close to the sensor, basically covering it. Store the measurements in an excel file together.
	- The basic idea is that you should have stable measurements for each of the sensors - one directly from the sensor, and one from the reference sensor.
4. **Repeat with other angles and environment setting:**
	- Rotate the calibration bech by 15°.
	- Take and store measurements until you reach the 90° mark.
	- repeat the whole process in a daylight room setting.
5. **Exmaple Calibration csv structure:**

| Angle | Sensor Number (ID) | Sensor Reading |
| ----- | ------------------ | -------------- |
| 0     | Sensor 0           | 500            |
| 0     | Sensor 1           | 532            |
| 0     | Sensor 2           | 498            |
| 0     | Sensor ....        | ---            |
| 0     | Sensor Reference 0 | 512            |
| 0     | Sensor Reference 1 | 543            |

5. **Compare and adjust**
	- Compare readings from sensors with the reference sensor on a graph
	- Apply the adjustments so the reading would cover each other and hard code them in the code of the measuring script.

## End
