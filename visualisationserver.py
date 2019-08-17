#
import eventlet
eventlet.monkey_patch()

from flask import Flask, render_template, send_file
from flask_socketio import SocketIO

app = Flask(__name__, static_folder="build/static", template_folder="build")
app.config['SECRET_KEY'] = '#super secret key!#'
socketio = SocketIO(app, message_queue='redis://127.0.0.1:6379/')

@app.route('/manifest.json')
def manifest():
    return send_file('build/manifest.json')

@app.route('/logo192.png')
def logo192():
    return send_file('build/logo192.png')

@app.route('/logo512.png')
def logo512():
    return send_file('build/logo512.png')

@app.route("/")
def index():
    return render_template('index.html')


def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json):
    print('received my event: ' + str(json))
    socketio.emit('my response', json)

if __name__ == '__main__':
    socketio.run(app, debug=True) #, port=5000, host='192.168.1.111')

