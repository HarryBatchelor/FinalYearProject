import mimetypes
from venv import create
from flask import Flask, render_template, request, Response, redirect
from camera import VideoCamera
import time
import threading
import os
import sqlite3
import Adafruit_ADXL345
from SaveToCSV import PoleHit

pi_camera = VideoCamera(flip = False) # flip pi camera if upside down

app = Flask(__name__)

dbname='sensordata.db'
sampleFreq = 1 #time in seconds

def main():
	while True:
		x, y, z, x2, y2, z2 = getADXLdata()
		logData(x, y, z, x2, y2, z2)
		time.sleep(sampleFreq)

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
        'z2': z2}
    return render_template('index.html', **templateData)

@app.route('/SaveToCSV/')
def CSVOutput():
	PoleHit()
	print('I got clicked!')
	return redirect('/', code=302)

@app.route('/camera')
def LiveStream():
		return render_template('LiveStream.html')
def gen(camera):
	#get camera frame
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
		
@app.route('/video_feed')
def video_feed():
	return Response(gen(pi_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

					
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=9000, debug=False)
   
   #192.168.0.144 192.168.0.129