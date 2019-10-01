#!/usr/bin/python3
from gpiozero import TimeOfDay, Energenie
from datetime import time
from time import sleep
from w1thermsensor import W1ThermSensor

#Setup
sensor1 = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, "000004d46a84")
daytime = TimeOfDay( time(8), time(17))
dayTemp = 18
nightTemp = 8
heater = Energenie(1)

def h_timer():
    if daytime.value:
        target = dayTemp
    else:
        target = nightTemp
    return target

def thermostat(target):
    temp_now = sensor1.get_temperature()
    if temp_now > (target+1):
        heater.off()
    elif temp_now < (target-1):
        heater.on()
        
while True:
    thermostat(h_timer())
    sleep(1)
    
