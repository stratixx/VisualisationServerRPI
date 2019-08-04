import eventlet
eventlet.monkey_patch()
from flask_socketio import SocketIO


socketio = SocketIO(message_queue='redis://192.168.1.111:6379/')
for x in range(1, 20):
    msg = 'daddy is talking to you: ' + str(x) + '!'
    socketio.emit('my response', {'user_name' : 'localTalker', 'message' : msg})
print('ok')
