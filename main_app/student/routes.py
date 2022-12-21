#   importing basic flask module
from flask import render_template
from flask import Blueprint
from flask import request
from flask import redirect
from flask import flash
from flask import url_for
from flask import jsonify

from main_app import db

from main_app.student.forms import AddStudent
from main_app.student.forms import AddStudentClasswise

from main_app.models import Student

#   initializing blueprint
student = Blueprint('student', __name__)

# ALL STUDENT LIST
@student.route('/students/', methods=['GET','POST'])
def students():
    form = AddStudent()
    students = Student.query.all()

    if form.validate_on_submit():
        student = Student(name=form.student_name.data, roll=form.student_roll.data, classname=form.student_class.data, address=form.address.data)
        db.session.add(student)
        db.session.commit()
        flash(f'Student {form.student_name.data} added successfuylly ✔', 'success')
        return redirect(url_for('student.students'))

    return render_template('student/allstudent.html', form=form, students=students)


# CLASS WISE STUDENT LIST
@student.route('/students/<string:classname>/', methods=['GET','POST'])
def student_classwise(classname):
    form = AddStudentClasswise()
    students = Student.query.all()

    if form.validate_on_submit():
        form.student_class.data = classname
        student = Student(name=form.student_name.data, roll=form.student_roll.data, classname=form.student_class.data, address=form.address.data)
        db.session.add(student)
        db.session.commit()
        flash(f'Student {form.student_name.data} added successfuylly ✔', 'success')
        return redirect(url_for('student.students'))

    return render_template('student/classwisestudentlist.html', form=form, students=students)


@student.route("/student/<int:student_id>/delete/", methods=['POST'])
def student_delete(student_id):
    student = Student.query.get_or_404(student_id)
    db.session.delete(student)
    db.session.commit()
    flash('Student has been deleted! ✔', 'success')
    return redirect(url_for('student.students'))   