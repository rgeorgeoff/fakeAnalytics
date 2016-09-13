#!/usr/bin/env python
from flask import Flask
import json

app = Flask(__name__)

@app.route('/')
def respond():
    try:
        return json.dumps("recieved get")
    except ClientException as e:
        return json.dumps(dict(error=e.message)), 404

@app.route('/test')
def respond_test():
    return json.dumps("recieved test get")

@app.route('/', methods=['POST'])
def respond_post():
    try:
        return json.dumps("recieved post")
    except ClientException as e:
        return json.dumps(dict(error=e.message)), 404

if __name__ == '__main__':
    app.run()
