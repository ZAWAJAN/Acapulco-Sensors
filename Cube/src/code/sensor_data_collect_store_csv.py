import smbus
import time
import csv
import argparse
from datetime import datetime

# Initialize the I2C bus
channel = 1
bus = smbus.SMBus(channel)

# Address of the TCA9548A multiplexer and sensors
tca_address = 0x70
light_sensor_address = 0x44
aht20_address = 0x38

# Function to select a channel on the TCA9548A
def select_channel(bus, channel):
    if channel < 0 or channel > 7:
        raise ValueError("Channel must be between 0 and 7")
    bus.write_byte(tca_address, 1 << channel)

# Byte swap function for the light sensor
def byte_swap(byte):
    tmp = (byte & 0xff) << 8
    tmp |= (byte >> 8)
    return tmp

# Function to read the lux from the light sensor
def read_lux(bus, address):
    devid = byte_swap(bus.read_word_data(address, 0x7f))
    manid = byte_swap(bus.read_word_data(address, 0x7e))

    config = 0b1100101000010000
    config = byte_swap(config)
    bus.write_word_data(address, 0x01, config)

    data = 0
    count = 0

    while data & 0b0000000010000000 == 0 and count < 20:
        count += 1
        byte_swap(bus.read_word_data(address, 0x01))
        time.sleep(0.01)

    data = byte_swap(bus.read_word_data(address, 0x00))

    E = (data & 0xf000) >> 12
    R = data & 0x0fff

    LSB_Size = 0.01 * (2 ** E)
    lux = LSB_Size * R
    lux_corrected = lux * 1.5 # The 1.5 is here as the first inintial calibration correction based on the code from the manufacturer.
    
    # After this, the final correction should be applied, based on the calibration process.

    return round(lux_corrected,3)

# Function to initialize and read temperature and humidity from AHT20
def read_temperature_humidity(bus, address):
    # Reset AHT20
    bus.write_byte(address, 0xBA)
    time.sleep(0.05)  # Short delay for reset
    
    # Initialize AHT20
    bus.write_byte_data(address, 0xAC, 0x33)
    time.sleep(0.1)  # Short delay for initialization

    # Trigger measurement
    bus.write_byte(address, 0xAC)

    # Wait for data to be ready
    time.sleep(0.1)  # Increased wait time for measurement

    # Read the data (6 bytes)
    data = bus.read_i2c_block_data(address, 0x00, 6)

    # Extract humidity and temperature values from data
    raw_humidity = ((data[1] << 12) | (data[2] << 4) | (data[3] >> 4)) & 0xFFFFF
    raw_temperature = ((data[3] & 0x0F) << 16) | (data[4] << 8) | data[5]

    humidity = (raw_humidity * 100) / 1048576
    temperature = (raw_temperature * 200 / 1048576) - 50

    return temperature, humidity

# Function to read values from all sensors once
def read_all_sensors_once():
    sensor_data = {}
    
    # Read from light sensors (channels 0-5)
    for ch in range(6):
        select_channel(bus, ch)
        lux_discard = read_lux(bus, light_sensor_address) # this is done to ensure the stored reading is not 0
        lux = read_lux(bus, light_sensor_address)
        sensor_data[f"lux{ch}"] = lux

    # Read from temperature & humidity sensor (channel 6)
    select_channel(bus, 6)
    temperature, humidity = read_temperature_humidity(bus, aht20_address)
    sensor_data["temp"] = temperature
    sensor_data["hum"] = humidity

    return sensor_data

# Function to create the CSV file if it doesn't exist and write headers
def create_csv_file(csv_file):
    try:
        with open(csv_file, 'x', newline='') as csvfile:
            writer = csv.writer(csvfile)
            # Writing the headers
            writer.writerow(["timestamp", "sensor", "value"])
    except FileExistsError:
        # File already exists, no need to create or write headers again
        pass

# Function to append sensor data into the CSV file
def append_to_csv(csv_file, sensor, value):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(csv_file, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([timestamp, sensor, value])

# Main function to read sensors and store data in the CSV file
def main():
    # Set up argument parser to get CSV filename
    parser = argparse.ArgumentParser(description='Collect sensor data and store it in a CSV file.')
    parser.add_argument('csv_file', type=str, help='The CSV file to store sensor data.')
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Create the CSV file with headers if it doesn't exist
    create_csv_file(args.csv_file)
    
    # Read sensor data
    sensor_data = read_all_sensors_once()
    
    # Append each sensor reading into the CSV file
    for sensor, value in sensor_data.items():
        append_to_csv(args.csv_file, sensor, value)
        print(f"Stored {sensor}: {value:.2f}")

# Execute the main function
if __name__ == "__main__":
    main()
