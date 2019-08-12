import os
from os import environ
from flask import Flask
from qrcodepkg.qrcode import qrcode

app = Flask(__name__)
app.config.from_object(os.getenv('APP_SETTINGS','config.DevelopmentConfig'))

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/<msg>')
def createqr(msg):
    return msg+'PNG'

if __name__ == '__main__':
    app.run(host=app.config.get('HOST'),port=app.config.get('PORT'))