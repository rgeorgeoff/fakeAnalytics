#!/usr/bin/env python
from flask import Flask, g, request, render_template, Response
from werkzeug.exceptions import BadRequest, NotFound, InternalServerError
from os import path
import json

app = Flask(__name__)

@app.route('/')
def respond():
    try:
        return json.dumps("recieved get")
    except ClientException as e:
        return json.dumps(dict(error=e.message)), 400

@app.route('/', methods=['POST'])
def respond_post():
    try:
        return json.dumps("recieved post")
    except ClientException as e:
        return json.dumps(dict(error=e.message)), 400

@app.errorhandler(400)
def bad_request(error):
    from werkzeug.exceptions import BadRequestKeyError
    if isinstance(error, BadRequestKeyError):
        return serve_json(error.code, error="Missing field '%s'" % error.message)
    if isinstance(error, ClientException):
        return serve_json(error.code, error=error.description)
    return serve_json(error.code, error=str(type(error)))

@app.errorhandler(404)
@app.errorhandler(500)
def err_handler(error):
    return serve_json(error.code, error=error.description)

if __name__ == '__main__':
    app.run()
