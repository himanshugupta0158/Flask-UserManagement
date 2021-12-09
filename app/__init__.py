from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# importing flask_bcrypt for hashing password and checking it
from flask_bcrypt import Bcrypt
# for managing login 
from flask_login import LoginManager
from os.path import join, dirname, realpath
from flask_mail import Mail
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = '5776ca5151016c5a9198bb1d95a09e0e'

# connection postgres db to flask
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:123456@localhost/'


# connecting to sqlalchemy db

# below is db connection path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///UserManagement.db'

# below is db variable for using db operation and creating tables in db.
db = SQLAlchemy(app)

# bcrypt hash password variable
bcrypt = Bcrypt(app)

# LoginManager variable
login_manager = LoginManager(app)

# setting login view here
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')


mail = Mail(app)




from app import routes