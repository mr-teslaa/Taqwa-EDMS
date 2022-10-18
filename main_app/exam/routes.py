from decimal import Subnormal
from main_app import db

#   importing basic flask module
from flask import render_template
from flask import Blueprint
from flask import request
from flask import redirect
from flask import flash
from flask import url_for
from flask import jsonify

from main_app.exam.forms import AddExamForm
from main_app.exam.forms import AddExamSubjectForm 
from main_app.exam.forms import AddStudentResultForm 

from main_app.models import Exam
from main_app.models import ExamSubject

#   initializing blueprint
exam = Blueprint('exam', __name__)


#   ADD EXAM 
@exam.route('/exam/add', methods=['GET','POST'])
def addexam():
    form = AddExamForm()
    exams = Exam.query.all()
    if form.validate_on_submit():
        exam = Exam(exam_name=form.exam_name.data)
        db.session.add(exam)
        db.session.commit()
        flash('Exam added successfuylly ✔', 'success')
        return redirect(url_for('exam.addexam'))

    return render_template('exam/addexam.html', form=form, exams=exams)

@exam.route("/exam/<int:exam_id>/delete/", methods=['POST'])
def exam_delete(exam_id):
    exam = Exam.query.get_or_404(exam_id)
    db.session.delete(exam)
    db.session.commit()
    flash('Your post has been deleted! ✔', 'success')
    return redirect(url_for('exam.addexam'))   


#   ADD EXAM SUBJECT
@exam.route('/exam/subject/add', methods=['GET', 'POST'])
def addexam_subject():
    form = AddExamSubjectForm()
    form.exam.choices = [(exam.id, exam.exam_name) for exam in Exam.query.all()]
    exam_subject = ExamSubject.query.all()
    if form.validate_on_submit():
        subject = ExamSubject(exam_subject=form.exam_subject_name.data.lower(), full_marks=form.full_marks.data, pass_marks=form.pass_marks.data,exam_id=form.exam.data)
        db.session.add(subject)
        db.session.commit()
        flash('Exam Subject added successfuylly ✔', 'success')
        return redirect(url_for('exam.addexam_subject'))

    return render_template('exam/addexamSubject.html', form=form, exam_subject=exam_subject)


@exam.route("/exam/subject/<int:exam_id>/delete/", methods=['POST'])
def exam_subject_delete(exam_id):
    exam = ExamSubject.query.get_or_404(exam_id)
    db.session.delete(exam)
    db.session.commit()
    flash('Your post has been deleted! ✔', 'success')
    return redirect(url_for('exam.addexam_subject'))  


#   ADD STUDENT RESULT
@exam.route('/exam/student/result', methods=['GET', 'POST'])
def addexam_student_result():
    form = AddStudentResultForm()
    form.exam.choices = [(exam.id, exam.exam_name) for exam in Exam.query.all()]
    exam_subject = ExamSubject.query.all()
    totalsubject=7
    if form.validate_on_submit():
        pass
        # subject = ExamSubject(exam_subject=form.exam_subject_name.data, full_marks=form.full_marks.data, pass_marks=form.pass_marks.data,exam_id=form.exam.data)
        # db.session.add(subject)
        # db.session.commit()
        # flash('Exam Subject added successfuylly ✔', 'success')
        # return redirect(url_for('exam.addexam_subject'))

    return render_template('exam/addexamStudentResult.html', form=form, exam_subject=exam_subject, totalsubject=totalsubject)


@exam.route('/exam/subject/marks/<string:subject>', methods=['GET', 'POST'])
def get_total_marks(subject):
    subjects = ExamSubject.query.filter_by(exam_subject=subject).all()

    subjectArray = []

    for subject in subjects:
        subobj = {}
        subobj['id'] = subject.id
        subobj['subject_name'] = subject.exam_subject
        subobj['full_marks'] = subject.full_marks
        subobj['pass_marks'] = subject.pass_marks
        subjectArray.append(subobj)

    return jsonify({'subjects': subjectArray})