import mimetypes
from flask import Flask,render_template,url_for,request,redirect, make_response, Response
import random
import json
from time import time
from random import random
import Adafruit_ADXL345
from camera import VideoCamera


app = Flask(__name__)
accel = Adafruit_ADXL345.ADXL345(address=0x53, busnum=4)
accel2 = Adafruit_ADXL345.ADXL345(address=0x53, busnum=4)
pi_camera = VideoCamera(flip=False)

@app.route('/', methods=["GET", "POST"])
def main():
    return render_template('index.html')

@app.route('/dataLeft', methods=["GET", "POST"])
def dataLeft():
    while True:
        x, y, z = accel.read()
        
        dataLeft= [time()*1000, x, y, z]
        
        response = make_response(json.dumps(data))

        response.content_type = 'application/json'

        return response
@app.route('/dataRight', method=["GET", "POST"])
def dataRight():
    while True:
        x2, y2, z2 = accel2.read()
        
        dataRight= [time()*1000, x2, y2, z2]
        
        response = make_response(json.dumps(data2))
        
        response.content_type = 'application/json'
        
        return response
@app.route('/camera')
def LiveStream():
    return render_template('LiveStream.html')
def gen(camera):
    #get camera frame
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(pi_camera),
                        mimetype = 'multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)