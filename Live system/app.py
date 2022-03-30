from socket import socket
from flask import Flask, render_template, url_for, copy_current_request_context
from flask_socketio import SocketIO, emit
from random import random
from time import sleep
from threading import Thread, Event

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True

#turn the flask app into a socketio app
socketio = SocketIO(app, async_mode=None, logger=True, engineio_logger=True)

thread = Thread()
thread_stop_event = Event()

def randomNumbergenerator():
    print("making numbers")
    while not thread_stop_event.is_Set():
        number = round(random()*10, 3)
        print(number)
        socketio.emit('newnumber', {'numbe':number}, namespace='/test')
        socketio.sleep(5)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect', namespace='/test ')
def test_connect():
    global thread
    print('Client connected')
    
    if not thread.isAlive():
        thread = socketio.start_background_task(randomNumbergenerator)

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')

if __name__ == '___main__':
    socketio.run(app)