from machine import I2C, Pin, SD
import ads1x15, time, machine, pycom, sys, utime, os
from adsx15read import adsx15read
import adcR # module needed in library for reading ADC and converting it to voltage
from math import sqrt
import sht31


def readsht31(messageNumber):
    i2c=I2C(baudrate=400000)
    sensor = sht31.SHT31(i2c = i2c, addr=0x44)
    (airTempCelsius,airRelHumidity)=sensor.get_temp_humi()
    print(airTempCelsius)
    print(airRelHumidity)
    return(airTempCelsius,airRelHumidity)
