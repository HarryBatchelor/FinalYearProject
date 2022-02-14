import time
import board
import busio
import adafruit_adxl34x
import smbus
import requests
import json

bus4 = smbus.SMBus(4)

i2c = busio.I2C(board.SCL, board.SDA)
accelerometer = adafruit_adxl34x.ADXL345(i2c)
print("%f %f %f"%accelerometer.acceleration)

BASE = 'http://192.168.0.129:5000'

print('Insert data : ')
response = requests.put(BASE + 'slalompole/', {"X" : X, "Y" : Y, "Z" : Z})
print(response.json())
