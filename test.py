import time
import Adafruit_ADXL345

accel = Adafruit_ADXL345.ADXL345(address=0x53, busnum=1)
accel2 = Adafruit_ADXL345.ADXL345(address=0x53, busnum=4)
# Alternatively you can specify the device address and I2C bus with parameters:

print ('Printing X, Y, Z axis values')

while True:
	x, y ,z = accel.read()
	x2, y2, z2 = accel2.read()
	print('X={0}, Y={1}, Z={2}'.format(x, y, z))
	print('X2={0}, Y2={1}, Z2={2}'.format(x2, y2,z2))
	time.sleep(0.5)
