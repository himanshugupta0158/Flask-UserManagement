from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = '5776ca5151016c5a9198bb1d95a09e0e'

# connection postgres db to flask
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:123456@localhost/'


# connecting to sqlalchemy db

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from app import routes