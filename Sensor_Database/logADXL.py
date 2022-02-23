import time
import sqlite3
import Adafruit_ADXL345

dbname='sensorsdata.db'
sampleFreq = 1 # time in seconds

# get data from DHT sensor
def getADXLdata():	
	
	accel = Adafruit_ADXL345.ADXL345()
	
	x, y, z = accel.read()
	


# log sensor data on database
def logData (x, y, z):
	
	conn=sqlite3.connect(dbname)
	curs=conn.cursor()
	
	curs.execute("INSERT INTO ACC_data values(datetime('now'), (?), (?), (?))", (x, y, z))
	conn.commit()
	conn.close()

def displayData():
	conn=sqlite3.connect(dbname)
	curs=conn.cursor()
	print ("\nEntire database contents:\n")
	for row in curs.execute("SELECT * FROM ACC_data"):
		print (row)
	conn.close()

# main function
def main():
	for i in range (0,3):
        getADXLdata()
        time.sleep(sampleFreq)
        displayData()

# ------------ Execute program 
main()