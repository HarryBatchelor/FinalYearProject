from flask import Flask,render_template,url_for,request,redirect, make_response
import random
import json
from time import time
from random import random
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def main():
    return render_template('index.html')

@app.route('/data', methods=["GET", "POST"])
def data():
    Tempreature = random()*100
    Humidity = random()*55

    data = [time() *1000, Tempreature, Humidity]

    response = make_response(json.dumps(data))
    response.content_type = 'application/json'

    return response

if __name__ == "__main__":
    app.run(host='192.168.0.150', port=5000, debug=True)