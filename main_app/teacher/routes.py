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
from main_app.models import Notice
from main_app.models import Student
from main_app.models import Parent
from main_app.models import Classroom

from main_app.teacher.forms import ApplyTeacherForm


#   initializing blueprint
teacher = Blueprint('teacher', __name__)




#   apply for a parents accout route
@teacher.route('/teacher/apply', methods=['GET', 'POST'])
def apply_teacher():
    form = ApplyTeacherForm()
    return render_template('apply_teacher.html', title='Teacher Application', form=form)




