#!/usr/bin/env python3

from flask import Flask, render_template
import datetime

app = Flask(__name__)
@app.route('/')
def index():
    templateData = {
        'title' :   'Hello!',
        'time'  :   datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return render_template('index.html', **templateData)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='192.168.1.123')
    
