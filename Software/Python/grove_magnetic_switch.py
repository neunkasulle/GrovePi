#!/usr/bin/env python
#
# GrovePi Example for using the Grove Magnetic Switch (http://www.seeedstudio.com/wiki/Grove_-_Magnetic_Switch)
#
# The GrovePi connects the Raspberry Pi and Grove sensors.  You can learn more about GrovePi here:  http://www.dexterindustries.com/GrovePi
#
# Have a question about this example?  Ask on the forums here:  http://www.dexterindustries.com/forum/?forum=grovepi
#
'''
## License
 GrovePi for the Raspberry Pi: an open source platform for connecting Grove Sensors to the Raspberry Pi.
 Copyright (C) 2015  Dexter Industries

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/gpl-3.0.txt>.
'''
import time
import grovepi

# Connect the Grove Magnetic Switch to digital port D3
# SIG,NC,VCC,GND
magnetic_switch = 3

grovepi.pinMode(magnetic_switch,"INPUT")

while True:
    try:
        print (grovepi.digitalRead(magnetic_switch))
        time.sleep(.5)

    except IOError:
        print ("Error")
