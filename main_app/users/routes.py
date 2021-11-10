#   importing basic flask module
from flask import Blueprint
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask import flash

#   importing module from flask login
from flask_login import current_user
from flask_login import login_required
from flask_login import login_user
from flask_login import logout_user


import bcrypt  # password hash generator
from main_app import db
from main_app.models import Notice
from main_app.models import User
from main_app.models import StudentsInfo
from main_app.users.forms import AdmissionForm
from main_app.users.forms import ApplyParentsForm
from main_app.users.forms import ApplyTeacherForm
from main_app.users.forms import LoginForm
from main_app.users.forms import DemoRegForm
from main_app.users.forms import LoginFormParents

# PIL (Phillow) for saving pictures
from main_app.users.utils import save_picture

#   initializing blueprint
users = Blueprint('users', __name__)


#   admission route
@users.route('/admission', methods=['GET', 'POST'])
@users.route('/admission/', methods=['GET', 'POST'])
def admission():
    form = AdmissionForm()
    if form.validate_on_submit():
        student = StudentsInfo(unique_id=form.unique_id.data, roll_id=form.roll_id.data, firstname=form.firstname, lastname=form.lastname.data, father_name=form.father_name.data, mother_name=form.mother_name.data, phone_number=form.phone_number.data, birth_cirtificate_no=form.birth_cirtificate_no.data, birth_date=form.birth_date.data, gender=form.gender.data, care_of=form.care_of.data, zip_code=form.zip_code.data, address=form.address.data, email=form.email.data, image_file=save_picture(form.image_file.data), signature=save_picture(form.signature.data), transportation_status=form.transportation_status.data, graduation_status=form.graduation_status.data)
    
        db.session.add(student)
        db.session.commit()
        print('===================== I am in. Success =====================')
        print(f'unique id: {form.unique_id.data}')
        print(f'roll id: {form.roll_id.data}')
        print(f'first: {form.firstname.data}')
        print(f'last: {form.lastname.data}')
        print(f'father_name: {form.father_name.data}')
        print(f'mother_name: {form.mother_name.data}')
        print(f'phone : {form.phone_number.data}')
        print(f'birth certificate: {form.birth_cirtificate_no.data}')
        print(f'gender: {form.gender.data}')
        print(f'care of: {form.care_of.data}')
        print(f'zip code: {form.zip_code.data}')
        print(f'address: {form.address.data}')
        print(f'email: {form.email.data}')
        print(f'image file: {form.image_file.data}')
        print(f'signature: {form.signature.data}')
        flash(f'Success')

    flash(f'I am out', 'danger')
    print('===================== Failed =====================')
    print(f'unique id: {form.unique_id.data}')
    print(f'roll id: {form.roll_id.data}')
    print(f'first: {form.firstname.data}')
    print(f'last: {form.lastname.data}')
    print(f'father_name: {form.father_name.data}')
    print(f'mother_name: {form.mother_name.data}')
    print(f'phone : {form.phone_number.data}')
    print(f'birth certificate: {form.birth_cirtificate_no.data}')
    print(f'gender: {form.gender.data}')
    print(f'care of: {form.care_of.data}')
    print(f'zip code: {form.zip_code.data}')
    print(f'address: {form.address.data}')
    print(f'email: {form.email.data}')
    print(f'image file: {form.image_file.data}')
    print(f'signature: {form.signature.data}')
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
# @users.route('/dashboard')
# def dashboard():
#     return render_template('dashboard.html', title='Dasboard')

    
#   student dashboard route (added by f shrabon)
@users.route('/student')
def student():
    return render_template('student_dashboard.html', title='Student Dashboard')

#   admin dashboard  route (added by f shrabon)
@users.route('/admin')
def admin():
    return render_template('admin_dashboard.html', title='Admin Dashboard')


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
