# ========================================================================== #
#                           Junior School and College
#                    A School Management System with FLASK
#   
#       Create by some intelligent programmer
#       Full CRUD facility
#   
#       Github: https://github.com/hacker-tesla/Junior_School_and_College
# ========================================================================== #


#   importin basic module for flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#   pass this app through flask
app = Flask(__name__)
db = SQLAlchemy(app)
from main_app import routes




