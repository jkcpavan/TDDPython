import os

class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = '\xbf\xb0\x11\xb1\xcd\xf9\xba\x8bp\x0c...'

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    HOST = '127.0.0.5'
    PORT = 8080


class TestingConfig(BaseConfig):
    DEBUG = False
    TESTING = True

class ProductionConfig(BaseConfig):
    DEBUG = False