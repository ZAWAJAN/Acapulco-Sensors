# Cube Device Sensors calibration

Before you assemble the final cubic device, first the lux sensors have to be calibrated, as there always might be some small differences between each sensor, that might differ even more from the true readings of proffessional grade sensors.

Here we assume you'll have to borrow a proper lux sensor like --sensor name-- for the calibration process.

The calibration process needs a rather stable light source, preferably two - artificial in a dark room, and a natural like a single window during an overcast day.

During callibration, all the sensors have to be as close as possible to each other. For this purpose, a custom laser cut calibration bench can be fabricated using provided [CAD files](Cube/src/CAD/xxx.dwg)

## Hardware Assembly

Laser cut and assemble the calibration bench

place the sensors in the bench slots

connect wires (wire diagram)

1. **Assembly Instructions:**
   - Follow the [enclosure assembly guide](docs/assembly.md).
   - Connect the "Ambient 2 Click" sensors to the TCA9548A multiplexer.
   - Wire the multiplexer to the Raspberry Pi Zero.
   
2. **Wiring Diagram:**
   ![Wiring Diagram](images/wiring_diagram.png)

## Software

Install dependencies

Update and Upgrade

Run a test to see if it stores data correctly

1. **Installation:**
   - Clone the repository:
     ```bash
     git clone https://github.com/yourusername/cubic-illuminance-sensor.git
     ```
   - Install required Python libraries:
     ```bash
     pip install -r requirements.txt
     ```
2. **Running the Software:**
   - Execute the main script to start capturing readings:
     ```bash
     python main.py
     ```
## Calibration Steps

Direct the sensors towards the light source

run the code to store the data from the calibrated sensors and record the reading from the base Sensor

rotate the setup by 15° and repeat

Repeat in another setting

Compare readings from sensors with the base sensor on a graph, apply the adjustment in the reading code.