# ========================================================================== #
#                           Junior School and College
#                    A School Management System with FLASK
#   
#       Create by some intelligent programmer
#       Full CRUD facility
#   
#       Github: https://github.com/hacker-tesla/Junior_School_and_College
# ========================================================================== #


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate




#   pass this app through flask
app = Flask(__name__)

app.config['SECRET_KEY'] = '248fb9a5bdffa13c0bc136504ebf75c2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypi = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from main_app import routes
from main_app.models import User
migrate = Migrate(app,db)