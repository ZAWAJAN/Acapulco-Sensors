# Acapulco Sensors

## Introduction

The Cube (cubic illuminance sensor) and the Camera (HDR image generation setup) sensors were developed as open hardware devices to support predictive building control as a part of the [Acapulco](https://www.thegreenvillage.org/project/acapulco/) research project at [TU Delft Green village](https://www.thegreenvillage.org/).
The Acapulco project, based in the TU Delft Green Village, the Netherlands, is developing innovative design tools to optimise the sustainability of heating and cooling systems in commercial buildings. The project focuses on integrating thermal storage, a heat pump with ground and surface water sources, and AI-powered predictive controls to enhance energy efficiency, reduce CO2 emissions, and alleviate grid congestion.

## Sensing Devices

The project uses two environmental sensing devices, which are sometimes referred to as "sensors" in this documantation. 
Each device is in fact a collection of various sensors and parts.
Both devices were used together in the Acapulco project, however, one can be used without the other.

In two separate folders you can find all needed instructions to assemble and use the two sensors:
1. [**The Cube**](Cube/)
	- A cubic open-source illuminance sensor designed for environmental monitoring (The Cube).
	- The Cube uses a Raspberry Pi Zero 2W with "Ambient 2 Click" sensors connected via a multiplexer, with additional temperature and humidity sensor, all enclosed in a laser-cut box.
2. [**The Camera**](Camera/)
	 - A camera setup for HDR image generation (The Camera).
	 - The Camera uses a Raspberry Pi 4B, with one additional "Ambient 2 Click" sensor for luminance validation. Attached to the ceiling by 3D-printed parts and standard camera mounting elements.

## Authors

The sensors design, production, and callibration was performed by:
- [Eleonora Brembilla](https://www.tudelft.nl/en/staff/e.brembilla/)
- [Pedro de la Barra Luegmayer](https://www.tudelft.nl/en/staff/p.delabarraluegmayer/)
- [Jan Zawadzki](https://www.linkedin.com/in/jan-zawadzki-a92650213/)
- [Wouter Beck](https://www.linkedin.com/in/wouterbeck/)
