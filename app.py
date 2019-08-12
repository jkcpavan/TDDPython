import os
from os import environ
from flask import Flask,request,abort
from qrcodepkg.qrcode import qrcode

app = Flask(__name__)
app.config.from_object(os.getenv('APP_SETTINGS','config.DevelopmentConfig'))

@app.route('/')
def hello():
    if request.headers['x_forwarded_proto'].lower()== "http":
       return abort(404)
    return 'Hello, World!'

@app.route('/<msg>')
def createqr(msg):
    if request.headers['x_forwarded_proto'].lower()== "http":
       return abort(404)
    return msg+'PNG'

if __name__ == '__main__':
    app.run(host=app.config.get('HOST'),port=app.config.get('PORT'))