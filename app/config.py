import os
from dotenv import load_dotenv

load_dotenv()  # load environment variables from .env if it exists.

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgres://hztvetvygllwog:8c7c80a849b15c6923823e0e0e0b9027db3defce93ae77d1619ffca14a37302d@ec2-3-225-213-67.compute-1.amazonaws.com:5432/d9t92ddtmou907')
    SQLALCHEMY_TRACK_MODIFICATIONS = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed