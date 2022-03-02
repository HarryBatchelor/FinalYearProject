from flask import Flask, render_template, request, Response
from camera import VideoCamera
import time
import threading
import os
import sqlite3
import Adafruit_ADXL345


pi_camera = VideoCamera(flip = False) # flip pi camera if upside down

app = Flask(__name__)

dbname='sensordata.db'
sampleFreq = 1 #time in seconds


#get data from sensor
# def getADXLdata():
# 	accel = Adafruit_ADXL345.ADXL345()

# 	x, y, z = accel.read()
# 	if x is not None and y is not None and z is not None:
# 		return x, y, z

# def logData(x, y, z):
# 	conn=sqlite3.connect(dbname)
# 	curs=conn.cursor()

# 	curs.execute("INSERT INTO ACC_data values(datetime('now'), (?), (?), (?))", (x, y, z))
# 	conn.commit()
# 	conn.close()

def main():
	while True:
		x, y, z, x2, y2, z2 = getADXLdata()
		logData(x, y, z, x2, y2, z2)
		time.sleep(sampleFreq)


# Retrieve data from database
@app.route('/record')
def getData():
	conn=sqlite3.connect('../sensorsdata.db')
	curs=conn.cursor()
	for row in curs.execute("SELECT * FROM ACC_data ORDER BY timestamp DESC LIMIT 1"):
		time = str(row[0])
		x = row[1]
		y = row[2]
		z = row[3]
		x2 = row[4]
		y2 = row[5]
		z2 = row[6]
	conn.close()
	return time, x, y, z, x2, y2, z2
# main route 
@app.route("/")
def index():	
	time, x, y, z, x2, y2, z2 = getData()
	templateData = {
		'time': time,
		'x': x,
		'y': y,
        'z': z,
		'x2': x2,
		'y2': y2,
        'z2': z2
	}
	return render_template('index.html', **templateData)


@app.route('/video_feed')
def video_feed():
	return Response(gen(pi_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

					
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=9000, debug=False)
   
   #192.168.0.144 192.168.0.129