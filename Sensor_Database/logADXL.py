import time
import sqlite3
import Adafruit_ADXL345

dbname='sensorsdata.db'
sampleFreq = 0.05# time in seconds

# get data from DHT sensor
def getADXLdata():

	accel = Adafruit_ADXL345.ADXL345(address=0x53, busnum=1)
	accel2 = Adafruit_ADXL345.ADXL345(address=0x53, busnum=4)


	x, y, z = accel.read()
	x2, y2, z2 = accel2.read()


	if x is not None and y is not None and z is not None and x2 is not None and y2 is not None and z2 is not None:

		return x, y, z, x2, y2, z2



# log sensor data on database
def logData (x, y, z, x2, y2, z2):

	conn=sqlite3.connect(dbname)
	curs=conn.cursor()

	curs.execute("INSERT INTO ALL_data values(datetime('now'), (?), (?), (?), (?), (?), (?))", (x, y, z, x2, y2, z2))
	conn.commit()
	conn.close()




#log data from 2nd accelerometer

# def logData2 (x2, y2, z2):
# 	conn=sqlite3.connect(dbname)
# 	curs=conn.cursor()
# 
# 	curs.execute("INSERT INTO ACC_data values(datetime('now'), (X2), (Y2), (Z2))", (x2, y2, z2))
# 	conn.commit()
# 	conn.close()


# main function
def main():
	while True:
		x, y, z, x2, y2, z2 = getADXLdata() 
		logData(x, y, z, x2, y2, z2)
		print('X={0}, Y={1}, Z={2}'.format(x, y, z))
		print('X2={0}, Y2={1}, Z2={2}'.format(x2, y2,z2))
		time.sleep(sampleFreq)

# ------------ Execute program
main()