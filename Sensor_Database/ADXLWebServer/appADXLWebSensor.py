from flask import Flask, render_template, request
from camera import VideoCamera
import time
import threading
import os
import sqlite3

pi_camera = VideoCamera(flip = False) # flip pi camera if upside down

app = Flask(__name__)

# Retrieve data from database

def getData():
	conn=sqlite3.connect('../sensorsdata.db')
	curs=conn.cursor()
	for row in curs.execute("SELECT * FROM ACC_data ORDER BY timestamp DESC LIMIT 1"):
		time = str(row[0])
		x = row[1]
		y = row[2]
		z = row[3]
	conn.close()
	return time, x, y, z
# main route 
@app.route("/")
def index():	
	time, x, y, z = getData()
	templateData = {
		'time': time,
		'x': x,
		'y': y,
        'z': z
	}
	return render_template('index.html', **templateData)

@app.route('/camera')
def LiveStream():
		return render_template('LiveStream.html')
def gen(camera):
	#get camera frame
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/vidoe_feed')
def video_feed():
	return Response(gen(pi_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

					
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000, debug=False)