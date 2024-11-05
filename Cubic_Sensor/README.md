# Cubic Illuminance Sensor

A modular open-source illuminance sensor designed for environmental monitoring. The device uses a Raspberry Pi Zero with "Ambient 2 Click" sensors connected via a multiplexer, all enclosed in a laser-cut box.

## Features
- Measures ambient light in multiple directions (cubic configuration).
- Modular and customizable design using off-the-shelf components.
- Built with open-source hardware and software principles.

## Table of Contents
1. [Introduction](#introduction)
2. [Bill of Materials (BOM)](#bill-of-materials-bom)
3. [Hardware Setup](#hardware-setup)
4. [Software Setup](#software-setup)
5. [Usage Instructions](#usage-instructions)
6. [Troubleshooting](#troubleshooting)
7. [Contributing](#contributing)
8. [License](#license)

## Introduction
The Cubic Illuminance Sensor is designed to measure light levels from different angles for environmental sensing applications. It's based on a Raspberry Pi Zero and multiple "Ambient 2 Click" sensors, offering a flexible and modular design.

## Bill of Materials (BOM)
| Component               | Quantity | Description                           | Link                       |
|-------------------------|----------|---------------------------------------|----------------------------|
| Raspberry Pi Zero       | 1        | Small form-factor computer            | [Buy here](#)               |
| Ambient 2 Click         | 6        | Light sensor module                   | [Buy here](#)               |
| TCA9548A Multiplexer    | 1        | I2C multiplexer for sensor connection | [Buy here](#)               |
| Laser-cut acrylic case  | 1        | Custom enclosure                      | [CAD Files](#)              |
| Miscellaneous hardware  | -        | Screws, spacers, wiring, etc.         | -                           |

## Hardware Setup
1. **Assembly Instructions:**
   - Follow the [enclosure assembly guide](docs/assembly.md).
   - Connect the "Ambient 2 Click" sensors to the TCA9548A multiplexer.
   - Wire the multiplexer to the Raspberry Pi Zero.
   
2. **Wiring Diagram:**
   ![Wiring Diagram](images/wiring_diagram.png)

## Software Setup
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

## Usage Instructions
- Describe how to use the sensor, adjust settings, and interpret the data.
- Provide examples, such as data logging or integration with other systems.

## Troubleshooting
- [Common Issues and Solutions](docs/troubleshooting.md)

## Contributing
- [Contribution Guidelines](docs/contributing.md)

## License
This project is licensed under the [MIT License](LICENSE).
