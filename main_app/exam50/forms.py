from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import IntegerField
from wtforms import PasswordField
from wtforms import SelectField
from wtforms import SubmitField
from wtforms import BooleanField
from wtforms.validators import DataRequired
from wtforms.validators import Length
from wtforms.validators import Email
from wtforms.validators import EqualTo

class AddMarksForm50(FlaskForm):
    roll_id = IntegerField(
        'Roll / ID',
        validators = [ DataRequired() ]
    )

    # classname = StringField(
    #     'Class Name',
    #     validators = [ DataRequired() ]
    # )

    examname = SelectField(
        'Exam Name',
        choices = [
            ('N/A', '-- Select Class --' ),
            ('1st', '1st Semister Examination' ),
            ('2nd', '2nd Semister Examination' ),
            ('3rd', '3rd Semister Examination' ),
            ('final', 'Final Examination' ),
            ('modeltest', 'Model Test' )
        ],
        validators = [ DataRequired() ]
    )

    examyear = IntegerField(
        'Examination Year',
        validators = [ DataRequired() ]
    )

    classname = SelectField(
        'Class',
        choices = [
            ('N/A', '-- Select Class --' ),
            ('play', 'play' ),
            ('nursary', 'nursary' ),
            ('one', 'one' ),
            ('two', 'two' ),
            ('three', 'three' ),
            ('four', 'four' ),
            ('five', 'five' ),
            ('six', 'six' ),        
            ('seven', 'seven' ),
            ('eight', 'eight' )
        ],
        validators = [ DataRequired() ]
    )

    name = StringField(
        'Student\'s Name',
        validators = [ DataRequired() ]
    )

    bengali = IntegerField(
        'Bengali',
        validators = [ DataRequired() ]
    )

    english = IntegerField(
        'English',
        validators = [ DataRequired() ]
    )

    mathematics = IntegerField(
        'Mathematics',
        validators = [ DataRequired() ]
    )

    science = IntegerField(
        'Science',
        validators = [ DataRequired() ]
    )

    bandg = IntegerField(
        'B & G',
        validators = [ DataRequired() ]
    )

    religion = IntegerField(
        'Religion',
        validators = [ DataRequired() ]
    )

    grade = StringField(
        'Grade',
        validators = [ DataRequired() ]
    )

    gpa = StringField(
        'GPA',
        validators = [ DataRequired() ]
    )

    total = IntegerField(
        'Total',
        validators = [ DataRequired() ]
    )

    submit = SubmitField('Submit')