#!/usr/bin/env python
from flask import Flask, render_template
import datetime
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    print('get index.html')
    templateData = {
        'title' :   'Hello!',
        'time'  :   datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return render_template('index.html', **templateData)

if __name__ == '__main__':
    socketio.run(app, debug=True, port=5000, host='192.168.1.111')
    
@socketio.on('my event')
def handle_my_custom_event(message):
    print('received message: ' + message)
    return 'ok'

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)
    return 'ok'

@socketio.on('connect')
def test_connect():
    #emit('my response', {'data': 'Connected'})
    print('Client connected')

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')
