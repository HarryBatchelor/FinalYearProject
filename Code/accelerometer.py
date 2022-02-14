import time
import board
import busio
import adafruit_adxl34x
import smbus

bus4 = smbus.SMBus(4)

i2c = busio.I2C(board.SCL, board.SDA)
accelerometer = adafruit_adxl34x.ADXL345(i2c)

while True:
    print("%f %f %f"%accelerometer.acceleration)
    time.sleep(1)
