#   importing basic flask module
from flask import render_template
from flask import Blueprint

#   importing module from flask login
from flask_login import login_user
from flask_login import current_user
from flask_login import logout_user
from flask_login import login_required

#   importing database uri
from main_app import db
from main_app import bcrypt    #password hash generator
from main_app.models import User
from main_app.models import Notice

from main_app.users.forms import AdmissionForm
from main_app.users.forms import ApplyParentsForm


#   initializing blueprint
users = Blueprint('users', __name__)]


#   admission route
@users.route('/admission', methods=['GET', 'POST'])
def admission():
    form = AdmissionForm()
    return render_tempate('admission.html', title='Admission', form=form)


#   apply for a parents accout route
@users.route('/parents/apply', methods=['GET', 'POST'])
def apply_parents():
    form = ApplyParentsForm()
    return render_tempate('apply_parents.html', title='Admission', form=form)

#   dashborad route
@users.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboared.html', title='Dasboard')


@users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


@users.route('/login/parents', methods=['GET', 'POST'])
def login_parents():
    form = LoginFormParents()
    return render_template('login_parents.html', title='Login', form=form)
