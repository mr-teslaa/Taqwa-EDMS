from flask import Blueprint
from flask import render_template
from flask import url_for
from flask import flash
from flask import redirect

import bcrypt
from main_app import db

from admindashboard.forms import RegistrationForm
from admindashboard.forms import SearchExamForm

from main_app.models import Marks50
from main_app.models import User
from main_app.models import Marks

from flask_login import login_user
from flask_login import current_user
from flask_login import logout_user
from flask_login import login_required

admindashboard = Blueprint('admindashboard', __name__)

@admindashboard.route('/dashboard', methods=['GET', 'POST'])
@admindashboard.route('/dashboard/', methods=['GET', 'POST'])
def dashboard():
    form = SearchExamForm()
    form.examname.data = '3rd'
    marks = Marks50.query.all()
    three = Marks50.query.filter_by(classname='three').all()
    return render_template('dashboard.html', marks=marks, form=form, three=three)

@admindashboard.route('/register', methods=['GET', 'POST'])
@admindashboard.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', form=form)

# delete student individual marks
@admindashboard.route('/delete/<string:classname>/<string:roll_id>/delete', methods=['GET', 'POST'])
@admindashboard.route('/delete/<string:classname>/<string:roll_id>/delete/', methods=['GET', 'POST'])
def deletestudent(classname, roll_id):
    student = Marks50.query.filter_by(classname=classname, roll_id=roll_id).first_or_404()
    db.session.delete(student)
    db.session.commit()
    flash(f'"{student.name}"\'s marks has been deleted!', 'success')
    return redirect(url_for('exam.viewmarks', classname=student.classname))