#   importing basic flask module
from flask import render_template
from flask import redirect
from flask import url_for
from flask import Blueprint
from flask import request

#   importing module from flask login
from flask_login import login_user
from flask_login import current_user
from flask_login import logout_user
from flask_login import login_required

#   importing database uri
from main_app import db
from main_app import bcrypt    #password hash generator
from main_app.models import User

from main_app.users.forms import AdmissionForm
from main_app.users.forms import LoginForm
from main_app.users.forms import LoginFormParents
from main_app.users.forms import ApplyParentsForm
from main_app.users.forms import ApplyTeacherForm
from main_app.users.forms import DemoRegForm


#   initializing blueprint
users = Blueprint('users', __name__)


#   admission route
@users.route('/admission', methods=['GET', 'POST'])
def admission():
    form = AdmissionForm()
    return render_template('admission.html', title='Admission', form=form)


#   apply for a parents accout route
@users.route('/parents/apply', methods=['GET', 'POST'])
def apply_parents():
    form = ApplyParentsForm()
    return render_template('apply_parents.html', title='Parents Application', form=form)

#   apply for a parents accout route
@users.route('/teacher/apply', methods=['GET', 'POST'])
def apply_teacher():
    form = ApplyTeacherForm()
    return render_template('apply_teacher.html', title='Teacher Application', form=form)

#   dashborad route
@users.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', title='Dasboard')


@users.route('/demo/register', methods=['GET', 'POST'])
def demo_register():
    form = DemoRegForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('users.login'))
    return render_template('demo_register.html', title='Demo Register', form=form)


@users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('users.dashboard'))
    return render_template('login.html', title='Login', form=form)


@users.route('/login/parents', methods=['GET', 'POST'])
def login_parents():
    form = LoginFormParents()
    return render_template('login_parents.html', title='Login', form=form)
