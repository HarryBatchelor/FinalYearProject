import time
import sqlite3
import Adafruit_ADXL345

dbname='sensorsData.db'
sampleFreq = 1 # time in seconds

# get data from DHT sensor
def getADXLdata():	
	
	accel = Adafruit_ADXL345.ADXL345()
	
	x, y, z = accel.read()
	


# log sensor data on database
def logData (x, y, z):
	
	conn=sqlite3.connect(dbname)
	curs=conn.cursor()
	
	curs.execute("INSERT INTO DHT_data values(datetime('now'), (?), (?), (?))", (x, y, z))
	conn.commit()
	conn.close()

# main function
def main():
	while True:
		x, y, z = getADXLdata()
		logData (x, y, z)
		time.sleep(sampleFreq)

# ------------ Execute program 
main()