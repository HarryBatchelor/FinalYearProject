import mimetypes
from venv import create
from flask import Flask, render_template, request, Response
from camera import VideoCamera
import time
import threading
import os
import sqlite3
import Adafruit_ADXL345
import pandas
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import io
import random


pi_camera = VideoCamera(flip = False) # flip pi camera if upside down

app = Flask(__name__)

dbname='sensordata.db'
sampleFreq = 1 #time in seconds

sql = """SELECT timestamp, x, y, z from ACC_data ORDER BY timestamp DESC LIMIT 10"""
data = pandas.read_sql(sql, conn)
plt.plot(data.timestamp, data.x, label = "X Coords")
plt.plot(data.timestamp, data.y, label = "Y Coords")
plt.plot(data.timestamp, data.z, label = "Z Coords")
plt.legend()
plt.title("Coords")



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
        'z2': z2}
    return render_template('index.html', **templateData)
@app.route('/plot.png')
def PlotPNG():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')
def create_figure():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    xs = range(100)
    ys = [random.randint(1,50) for x in xs]
    axis.plot(xs, ys)
    return fig

@app.route('/video_feed')
def video_feed():
	return Response(gen(pi_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

					
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=9000, debug=False)
   
   #192.168.0.144 192.168.0.129