# Cubic Enclosure Assembly Guide

After sensors calibration, you can assemble the final cubic device. This guide will help you assemble the laser-cut enclosure for the Cubic Illuminance Meter.

## Required Tools
- Laser-cut acrylic panels
- Milky white tape (to cover sensor holes)
- Masking tape (easily removable)
- Black matte spray paint
- Glue (normal hobby wood glue will suffice)
- Hot glue
- Screwdriver with hexagonal bit
- Strong string

## Assembly Steps
1. **Prepare the Cube Panels:**
	- Laser cut the elements of the cube using the provided [CAD file](../src/hardware/Cube_Box_Enclosure.dwg).
	- Identify each panel after cutting - number them according to which sensor will placed on each one (for easier reference).
	- **Note!** Try assembling the box in your hands, make sure everything fits together.

2. **Spray painting:**
	- Put the milky tape on the outsides of each panel to cover the sensor holes. As explained earlier, this tape enables the light to be more scattered and even.
	- From the masking paper tape - cut circes the size of holes - and put them on the tape covering the holes. This will prevent the black paint from staining the sesnor openinigs.
	- You can also cover the holes on the inward side - to make sure nothing contaminates the tape form the other side.
	- Apply black matte spray paint on the outsides of the panels.

3. **Panel Preparation:**
	- Remove the masking tape from the inside of each panel.
	- Glue the sensor barckets to each panel according to the engraved outline.
	- Glue the little bolt holders to the top panel. You can see small square holes for that purpose. You can already glue the bolt nuts to the insides of the bold holder elements. 

4. **Attach the Sensors:**
	- Secure each _"Ambient 2 Click"_ sensor inside the enclosure bracket. The sensor itself should be in the middle of the hole.
	- Each sensor should be numbered, as during calibration, so now you can put the sensors in the same numbered panel.
	- Tape the sensors so they are secured properly.

5. **Install the Raspberry Pi, Multiplexer, and the Temp Meter:**
	- Mount the Raspberry Pi on the PoE HAT (if you haven't done so already). Mount the heatsink on top of the Raspberry Pi. Use the screws and spacers provided with the extensions.
	- Mount the RPi brick in the designated spot on the bottom panel. Use the bolts and spacers to secure it in place.
	- Do the same with the TCA9548A Multiplexer and the Temperature and Humidity Sensor. The temperature sensor shpuld face the outside through the hole that is there for this purpose.
	- Ensure connections are secure.

6. **Final Assembly:**
	- We recommend starting with wiring the bottom panel elements with 3 side panels. This way you leave one of the side panels and the top panel for later, making it easier to connect things inside.
	- Refer to the same [Wiring Diagram](Images/Wiring_Diagram.png) as during the calibration process.
	- Use the hot glue to secure wires in place, so they don't eject spontaniously after the case is closed.
	- Join the panels together using glue. It can be a bit of a spaghetti inside, so be patient and carefull.
	- **Note!** Remember about the Ethernet cable for the Raspberry Pi. Best to plug it in before the 4th and top walls are in place. The ethernet cable goes though the hole in the top panel.
	- At this point you can also wire through the strings that will hold the cube in the air. Use the little holesin the corners of the bottom and top panels. Refer to the [String Mount Diagram](Images/Cube_String_Mount_Diagram.png).
	- Put the top panel in place. Secure it with bolts through the 4 holes in the side panels. The bolts should go though the holes, bolt holders and bolt nuts glued to the bolt holders. This way it's secured nicely and can be easily dismantled in case a need for a quick repair arises.
	- Tighten all connections and make sure if you did not forget about anything.
7. **Final Placement:**
	- Now the software should be tested to see whether you get eny data and if some of the connections did not get loose.
	- Remove the masking tape from the holes.
	- Hang the cube attatching it to the ceiling or something else. That highly depends on your setting.
