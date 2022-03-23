from flask import Flask
from .config import Config 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

UPLOAD_FOLDER = './app/static/uploads'

SECRET_KEY = 'Som3$ec5etK*y'

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Postgres@localhost:5432/Project1'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db = SQLAlchemy(app)
migrate = Migrate(app,db)

from app import views