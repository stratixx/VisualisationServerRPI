!# /env/bin/sh
python3 -m pip install --user virtualenv
python3 -m venv env
source env/bin/activate
pip3 install eventlet flask flask_socketio redis

#to deactivate:
#deactivate
