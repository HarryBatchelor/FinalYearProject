import time
import sqlite3
import Adafruit_ADXL345

dbname='sensorsdata.db'
sampleFreq = 1# time in seconds

# get data from DHT sensor
def getADXLdata():

	accel = Adafruit_ADXL345.ADXL345(address=0x53, busnum=1)
	

	x, y, z = accel.read()
	
	
	if x is not None and y is not None and z is not None:
		
		return x, y, z

	

# log sensor data on database
def logData (x, y, z):

	conn=sqlite3.connect(dbname)
	curs=conn.cursor()

	curs.execute("INSERT INTO ACC_data values(datetime('now'), (?), (?), (?))", (x, y, z))
	conn.commit()
	conn.close()


#define second accelerometer
def getADXLdata2():
	accel2 = Adafruit_ADXL345.ADXL345(address=0x53, busnum=4)

	x2, y2, z2 = accel2.read()

	if x2 is not None and y2 is not None and z2 is not None:

		return x2, y2, z2

#log data from 2nd accelerometer

def logData2 (x2, y2, z2):
	conn=sqlite3.connect(dbname)
	curs=conn.cursor()

	curs.execute("INSERT INTO ACC_data values(datetime('now'), (?), (?), (?))", (x2, y2, z2))
	conn.commit()
	conn.close()


# main function
def main():
	while True:
		x, y, z = getADXLdata()
		x2, y2, z2 = getADXLdata2()
		logData(x, y, z)
		logData2(x2, y2, z2)
		time.sleep(sampleFreq)

# ------------ Execute program
main()


