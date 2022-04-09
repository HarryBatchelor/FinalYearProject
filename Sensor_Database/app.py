from flask import Flask, render_template, request, Response, redirect
from camera import VideoCamera
from time import sleep 
import sqlite3
import Adafruit_ADXL345
from SaveToCSV import PoleHitRIGHT, PoleHitLEFT


# pi_camera = VideoCamera(flip = False) flip pi camera if upside down

app = Flask(__name__)

dbname='sensordata.db'
sampleFreq = 1 #time in seconds

def main():
	while True:
		x, y, z, x2, y2, z2 = getADXLdata()
		logData(x, y, z, x2, y2, z2)
		sleep(sampleFreq)


# Retrieve data from database
@app.route('/record')
def getData():
	conn=sqlite3.connect('sensorsdata.db')
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
        'z2': z2}
    return render_template('index.html', **templateData)

# @app.route('/camera')
# def LiveStream():
# 		return render_template('LiveStream.html')
# def gen(camera):
# 	#get camera frame
# 	while True:
# 		frame = camera.get_frame()
# 		yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
		
# @app.route('/video_feed')
# def video_feed():
# 	return Response(gen(pi_camera),
#                     mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/SaveToCSVRIGHT/')
def CSVOutput():
	PoleHitRIGHT()
	print('I got clicked RIGHT!')
	return redirect('/', code=302)

@app.route('/SaveToCSVLEFT/')
def CSVLEFT():
    PoleHitLEFT()
    print('I got clicked LEFT!')
    return redirect('/', code=302)
					
if __name__ == "__main__":
   app.run(host='192.168.0.75', port=5000, debug=False)
   




