# import time
# from board import *
# import busio
# import adafruit_adxl34x
# import smbus

# bus4 = smbus.SMBus(4)

# i2c = busio.I2C(board.SCL, board.SDA)
# accelerometer = adafruit_adxl34x.ADXL345(i2c)

# while True:
#     print("%f %f %f"%accelerometer.acceleration)
#     time.sleep(1)


import smbus
import time
from time import sleep
import sys

bus = smbus.SMBus(1)
bus4 = smbus.SMBus(4)

bus.write_byte_data(0x53, 0x2C, 0x0B)
value = bus.read_byte_data(0x53, 0x31)
value &= ~0x0F;
value |= 0x0B;  
value |= 0x08;
bus.write_byte_data(0x53, 0x31, value)
bus.write_byte_data(0x53, 0x2D, 0x08)

def getAxes():
    bytes = bus.read_i2c_block_data(0x53, 0x32, 6)
        
    x = bytes[0] | (bytes[1] << 8)
    if(x & (1 << 16 - 1)):
        x = x - (1<<16)

    y = bytes[2] | (bytes[3] << 8)
    if(y & (1 << 16 - 1)):
        y = y - (1<<16)

    z = bytes[4] | (bytes[5] << 8)
    if(z & (1 << 16 - 1)):
        z = z - (1<<16)

    x = x * 0.004 
    y = y * 0.004
    z = z * 0.004

    x = x * 9.80665
    y = y * 9.80665
    z = z * 9.80665

    x = round(x, 4)
    y = round(y, 4)
    z = round(z, 4)

    print("   x = %.3f ms2" %x)
    print("   y = %.3f ms2" %y)
    print("   z = %.3f ms2" %z)
    print("\n\n")
    
    return {"x": x, "y": y, "z": z}

bus.write_byte_data(0x53, 0x2C, 0x0B)
value = bus.read_byte_data(0x53, 0x31)
value &= ~0x0F;
value |= 0x0B;  
value |= 0x08;
bus.write_byte_data(0x53, 0x31, value)
bus.write_byte_data(0x53, 0x2D, 0x08)

def getAxes():
    bytes = bus.read_i2c_block_data(0x53, 0x32, 6)
        
    x = bytes[0] | (bytes[1] << 8)
    if(x & (1 << 16 - 1)):
        x = x - (1<<16)

    y = bytes[2] | (bytes[3] << 8)
    if(y & (1 << 16 - 1)):
        y = y - (1<<16)

    z = bytes[4] | (bytes[5] << 8)
    if(z & (1 << 16 - 1)):
        z = z - (1<<16)

    x = x * 0.004 
    y = y * 0.004
    z = z * 0.004

    x = x * 9.80665
    y = y * 9.80665
    z = z * 9.80665

    x = round(x, 4)
    y = round(y, 4)
    z = round(z, 4)

    print("   x = %.3f ms2" %x)
    print("   y = %.3f ms2" %y)
    print("   z = %.3f ms2" %z)
    print("\n\n")
    
    return {"x": x, "y": y, "z": z}
    
try:
    while True: 
        getAxes()
        time.sleep(2)
except KeyboardInterrupt:
    sys.exit()