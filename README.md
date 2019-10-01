# PiHeater
This repository contains the two Python 3 files used in the workshop heater project in my book <b>'Pi Projects and Programming'</b>.
To download these files to the Pi. Open a terminal session (Ctl-Atl-T) and enter:
git clone https://github.com/g4wnc/PiHeater.git
This will download the files and create a new directory called PiHeater where you'll find the files.

<b>PlugTest.py</b>
This is a simple program to pair and test an Energenie mains socket.
Use the program as follows:

1 - Begin by mounting the Energenie PiMote radio board on the Raspberry Pi GPIO pins.
2 - Power-up the Pi and go to the Programming menu and select Thonny Python IDE.
3 - Open the PlugTest.py file in Thonny (you will find it in ~/PiHeater/).
4 - Plug the Energie switchable socket ito a standard mains socket.
5 - Press and hold the button until the LED flashes to indicate that the socket is in programming mode.
6 - When the socket detects a transmission from the Pi, it will store the connection detail and start switching on and off.
7 - Click the STop button in Thonny to stop the program.

<b>PiHeater.py</b>
A simple workshop heater controller that uses an Energenie PiMote and Energenie RF controlled mains socket to control the heater. The thermal sensor is the popular DS18B20 device.
The Setup section of PiHeater.py has the preset values for on/off times and day/night temperatures. These can be altered to match the situation.

<b>Mike - G4WNC</b>
