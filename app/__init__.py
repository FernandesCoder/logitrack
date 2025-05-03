from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../app.db'
app.config['SECRET_KEY'] = 'secretkey'

db = SQLAlchemy(app)

from app import routes, models