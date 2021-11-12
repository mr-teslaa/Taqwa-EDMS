#   importing basic flask module
from flask import render_template
from flask import redirect
from flask import url_for
from flask import Blueprint
from flask import request
from flask.helpers import flash

#importing module from sqlachemy
from sqlalchemy import func

#   importing module from flask login
from flask_login import login_user
from flask_login import current_user
from flask_login import logout_user
from flask_login import login_required
import flask_login

#   importing database uri
from main_app import db
from main_app import bcrypt    #password hash generator
from main_app.models import Student
from main_app.models import Parent
from main_app.models import Classroom
from main_app.models import Roles


from main_app.parent.forms import LoginFormParents
from main_app.parent.forms import ApplyParentsForm



#   initializing blueprint
parent = Blueprint('parent', __name__)


#   apply for a parents accout route
@parent.route('/parent/apply', methods=['GET', 'POST'])
def apply_parents():
    form = ApplyParentsForm()

    if form.validate_on_submit():
        
        student_full_name = form.student_name_lastname.data.split(' ')
        firstname, lastname = student_full_name[0:-1], student_full_name[-1]

        firstname = ' '.join(firstname)
        
        classroom = Classroom.query.filter_by(class_name = form.student_class.data.upper()).first()
        student = Student.query.filter_by(first_name = firstname, last_name = lastname,
        student_roll = form.student_roll.data, classroom_id = classroom.id).first()

        if student:

            role = Roles.query.filter_by(role = 'Parent').first()
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

            Parent.query.filter_by(student_roll = form.student_roll.data).\
                update({Parent.first_name:form.name.data, Parent.last_name : lastname, 
                Parent.phone:form.phone_number.data, Parent.email: form.email.data,
                Parent.password : hashed_password, Parent.role_id : role.id})
        
            db.session.commit()
            flash('Parent successfully created.')

        else:
            flash('Student does not exist, please check values.')

        return redirect(url_for('parent.apply_parents'))


    return render_template('apply_parents.html', title='Parents Application', form=form)

#   login parent
@parent.route('/parent/login', methods=['GET', 'POST'])
def login_parents():
    form = LoginFormParents()
    if form.validate_on_submit():
        parent = Parent.query.filter_by(email = form.email.data, 
        student_roll = form.student_roll.data).first()
        if parent and bcrypt.check_password_hash(parent.password, form.password.data):
            login_user(parent, Parent)

            #   Test Parent Log-in
            return current_user.first_name
            

    return render_template('login_parents.html', title='Login', form=form)