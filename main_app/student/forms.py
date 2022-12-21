from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import TextAreaField
from wtforms import SubmitField
from wtforms import SelectField
from wtforms import IntegerField

#   wtf validators
from wtforms.validators import DataRequired
from wtforms.validators import Length
from wtforms.validators import EqualTo



class AddStudent(FlaskForm):
    student_name = StringField(
        'Student name',
        validators=[DataRequired()]
    )

    student_roll = IntegerField(
        'Student Roll',
        validators=[DataRequired()]
    )

    student_class = SelectField(
        'Exam', 
        choices=[
            ('play', 'PLAY'),
            ('nursary', 'NURSARY'),
            ('one', 'ONE'),
            ('two', 'TWO'),
            ('three', 'THREE'),
            ('four', 'FOUR'),
            ('five', 'FIVE'),
            ('six', 'SIX'),
            ('seven', 'SEVEN'),
            ('eight', 'EIGHT'),
        ],
        validators=[DataRequired()]
    )

    address = TextAreaField('Address')

    submit = SubmitField('Add student')


class AddStudentClasswise(FlaskForm):
    student_name = StringField(
        'Student name',
        validators=[DataRequired()]
    )

    student_roll = IntegerField(
        'Student Roll',
        validators=[DataRequired()]
    )

    student_class = StringField(
        'Class', 
        validators=[DataRequired()]
    )

    address = TextAreaField('Address')

    submit = SubmitField('Add student')