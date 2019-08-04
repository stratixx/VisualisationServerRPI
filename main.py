import eventlet
eventlet.monkey_patch()
import sys
from flask import Flask, render_template
from flask_socketio import SocketIO

global address
global app
global socketio

app = Flask(__name__)
    
def displayHelp():
    print('Typical usage: ')
    print('python3 main.py <host address>')
    print('Examples:')
    print('python3 main.py 192.168.1.201')
    print('python3 main.py localhost')
    print('python3 main.py --> will connect to localhost by default')
    
    
if __name__ == '__main__':
    
    if len(sys.argv)>1:
        if sys.argv[1]=='-h':
            displayHelp()
            exit()            
        address = sys.argv[1]
    else:
        address = 'localhost'
    print('IP addres: '+address)
    app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
    socketio = SocketIO(app, message_queue='redis://'+address+':6379/')
    socketio.run(app, debug=True, port=5000, host=address)
    

@app.route('/')
def index():
    print('index')
    return render_template('index.html')

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json):
    print('received my event: ' + str(json))
    socketio.emit('my response', json)

