from socketserver import DatagramRequestHandler
from tokenize import String
from unittest import result
from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import TextAreaField
from wtforms import PasswordField
from wtforms import SubmitField
from wtforms import SelectField
from wtforms import BooleanField
from wtforms import IntegerField
from wtforms import FileField

#   wtf validators
from wtforms.validators import DataRequired
from wtforms.validators import Length
from wtforms.validators import Email
from wtforms.validators import EqualTo


class AddExamForm(FlaskForm):
    exam_name = StringField(
        'Subject name',
        validators = [ DataRequired() ]
    )

    submit = SubmitField('Confirm')



class AddExamSubjectForm(FlaskForm):
    exam_subject_name = StringField(
        'Exam Subject name',
        validators = [ DataRequired() ]
    )

    full_marks = StringField(
        'Full Marks',
        validators = [ DataRequired() ]
    )

    pass_marks = StringField(
        'Pass Mark',
        validators = [ DataRequired() ] 
    )

    exam = SelectField(
        'Exam', 
        choices=[],
        validators=[DataRequired()]
    )

    submit = SubmitField('Cofirm')



class AddStudentResultForm(FlaskForm):
    student_name = StringField(
        'Student name'
    )

    student_roll = IntegerField(
        'Student Roll'
    )

    student_class = StringField(
        'Student Class'
    )

    exam = SelectField(
        'Exam', 
        choices=[],
        validators=[DataRequired()]
    )

    exam_subject_name = SelectField(
        'Exam Subject name',
        choices=[],
        validators = [ DataRequired() ]
    )

    full_marks = StringField('Full Marks')

    grade = StringField(
        'Grade'
    )

    achive_mark = StringField(
        'Achive Mark'
    )

    total_marks = StringField(
        'Total Marks'
    )    

    total_achive_mark = StringField(
        'Total Achive Marks'
    )    

    total_achive_grade = StringField(
        'Total Grade'
    )

    result_note = TextAreaField('Result Note')

    submit = SubmitField('Add Result')