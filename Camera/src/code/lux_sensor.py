import sys
import time
import smbus

# I2C bus and sensor address
bus = smbus.SMBus(1)  # Use I2C bus 1
sensor_address = 0x44  # Ambient 2 Click sensor address

def byte_swap(byte):
    tmp = (byte & 0xff) << 8
    tmp |= (byte >> 8)
    return tmp

def read_lux(bus, address):
    # Optional: Check device ID and manufacturer ID
    devid = byte_swap(bus.read_word_data(address, 0x7f))
    manid = byte_swap(bus.read_word_data(address, 0x7e))

    # Sensor configuration
    config = 0b1100101000010000
    config = byte_swap(config)
    bus.write_word_data(address, 0x01, config)

    data = 0
    count = 0

    # Wait until sensor is ready (or timeout after 20 tries)
    while data & 0b0000000010000000 == 0 and count < 20:
        count += 1
        byte_swap(bus.read_word_data(address, 0x01))
        time.sleep(0.01)

    # Read lux data
    data = byte_swap(bus.read_word_data(address, 0x00))

    # Convert to lux using the formula from your code
    E = (data & 0xf000) >> 12
    R = data & 0x0fff
    LSB_Size = 0.01 * (2 ** E)
    lux = LSB_Size * R

    # Adjust lux value
    return lux * 1.5

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python lux_sensor.py <output_file.txt>")
        sys.exit(1)

    output_file = sys.argv[1] + ".txt"

    lux = 0.0
    num_readings = 4  # Number of readings to take

    for i in range(num_readings):
        lux = read_lux(bus, sensor_address)
        print(f"Reading lux {i+1}: {lux}")
        time.sleep(0.3)  # Wait 0.3 seconds between readings

    # Save the last lux value to a file
    if lux is not None:
        with open(output_file, "w") as file:
            file.write(f"{lux}")
        print(f"Last lux value saved to {output_file}")
    else:
        print("Failed to read lux value.")
