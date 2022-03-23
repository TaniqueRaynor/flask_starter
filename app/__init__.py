from flask import Flask
from .config import Config 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

UPLOAD_FOLDER = './app/static/uploads'

SECRET_KEY = 'Som3$ec5etK*y'

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://hztvetvygllwog:8c7c80a849b15c6923823e0e0e0b9027db3defce93ae77d1619ffca14a37302d@ec2-3-225-213-67.compute-1.amazonaws.com:5432/d9t92ddtmou907'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db = SQLAlchemy(app)
migrate = Migrate(app,db)

from app import views