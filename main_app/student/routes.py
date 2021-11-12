#   importing basic flask module
from flask import render_template
from flask import redirect
from flask import url_for
from flask import Blueprint


#importing module from sqlachemy
from sqlalchemy import func


#   importing database uri
from main_app import db
from main_app.models import Student
from main_app.models import Parent
from main_app.models import Classroom
from main_app.models import Roles

from main_app.student.forms import AdmissionForm



#   initializing blueprint
student = Blueprint('student', __name__)


#   admission route
@student.route('/student/admission', methods=['GET', 'POST'])
def admission():
    form = AdmissionForm()

    if form.validate_on_submit():

        classroom = Classroom.query.filter_by(class_name = form.applicable_class.data.upper()).first()
        role = Roles.query.filter_by(role = 'Student').first()
        student = Student(first_name = form.firstname.data, last_name = form.lastname.data, 
                        father_name = form.father_name.data, mother_name = form.mother_name.data,
                        phone = form.phone_number.data, birth_cirtificate = form.birth_cirtificate_no.data,
                        date_of_birth = form.birth_date.data, address = form.address.data,
                        male = form.male.data, female = form.female.data ,email = form.email.data,
                        transportation = form.yes.data, password = form.password.data,
                        classroom_id = classroom.id, role_id = role.id)     
                              
        db.session.add(student)
        db.session.commit()

        parent = Parent(student_roll = student.student_roll)
        db.session.add(parent)
        db.session.commit()
        return redirect(url_for('student.admission'))

    return render_template('admission.html', title='Admission', form=form)

