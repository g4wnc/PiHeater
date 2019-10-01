#!/usr/bin/python3
from gpiozero import Energenie
from time import sleep
heater = Energenie(1)
while True:
    heater.on()
    sleep(2)
    heater.off()
    sleep(4)
    