from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField, FileField, PasswordField
       
#   wtf validators
from wtforms.validators import DataRequired, Email, EqualTo

#   make a Apply Form for Parent
class ApplyParentsForm(FlaskForm):

    #   make name field
    name = StringField(
        'Name',
        validators = [ DataRequired() ]
    )

    #   make username for teacher
    username = StringField(
        'Username',
        validators = [ DataRequired() ]
    )

    #   make phone number filed
    phone_number = IntegerField(
        'Phone Number',
        validators = [ DataRequired() ]
    )

    #   make email field
    email = StringField(
        'Email',
        validators = [
            DataRequired(),
            Email()
        ] 
    )

    #   make student name field
    student_name = StringField(
        'Student Name',
        validators = [ DataRequired() ]
    )

    #   make a select field for class
    student_class = SelectField(
        'Student Class',
        choices = [
            ('n/a', '--- Select Class ---'), ('play', '00 - PLAY'),
            ('nursary', '00 - NURSARY'), ('one', '01 - ONE'),
            ('two', '02 -TWO'), ('three', '03 - THREE'),
            ('four', '04 - FOUR'), ('five', '05 - FIVE'),
            ('six', '06 - SIX'), ('seven', '07 - SEVEN'),
            ('eight', '08 - EIGHT'), ('nine', '09 - NINE'),
            ('ten', '10- TEN')
        ]
    )

    #   make a student roll field
    student_roll = StringField(
        'Student Roll',
        validators = [ DataRequired() ]
    )

    #   make a student id field
    student_id = IntegerField(
        'Student ID',
        validators = [ DataRequired() ]
    )

    #   make password field
    password = PasswordField(
        'Password',
        validators = [ DataRequired() ]
    )

    #   make cofirm password
    confirm_password = PasswordField(
        'Confirm Password',
        validators = [
            DataRequired(),
            EqualTo(password)
        ]
    )

    #   make filed for photo
    photo = FileField(
        'Parent\'s Photo',
        validators = [ DataRequired() ]
    )

    #   make field for signature
    signature = FileField(
        'Signature',
        validators = [ DataRequired() ]
    ) 

    #   make a submit buton
    submit = SubmitField( 'Submit' )

