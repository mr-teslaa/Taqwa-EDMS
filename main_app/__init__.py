# ========================================================================== #
#                           Junior School and College
#                    A School Management System with FLASK
#   
#       Create by some intelligent programmer
#       Full CRUD facility
#   
#       Github: https://github.com/mr-teslaa/Junior_School_and_College
# ========================================================================== #







from flask import Flask


# import essential module for database
from flask_sqlalchemy import SQLAlchemy


# pass this application in flask
app = Flask(__name__)

# genarate a secret key
app.config['SECRET_KEY'] = '248fb9a5bdffa13c0bc136504ebf75c2'

# connect datbase to website
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# pass this application in sql_alchemy
db = SQLAlchemy(app)


# importing routes from routes.py
from main_app import routes 