from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import PasswordField
from wtforms import SubmitField
from wtforms import SelectField
from wtforms import IntegerField
from wtforms import FileField

#   wtf validators
from wtforms.validators import DataRequired
from wtforms.validators import Email
from wtforms.validators import EqualTo
from wtforms.validators import Length



class ApplyParentsForm(FlaskForm):
    
    #   make name field
    name = StringField(
        'Name',
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
    student_name_lastname = StringField(
        'Your children\'s name and lastname',
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
    student_roll = IntegerField(
        'Student Roll',
        validators = [ DataRequired() ]
    )

    '''
    #   make a student id field
    student_id = IntegerField(
        'Student ID',
        validators = [ DataRequired() ]
    )
    '''

    #   make password field
    password = PasswordField(
        'Password',
        validators = [ 
            DataRequired(),
            EqualTo('confirm_password', message = 'Passwords must be match')   
        ]
    )

    #   make cofirm password
    confirm_password = PasswordField(
        'Confirm Password',
        validators = [
            DataRequired()
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



class LoginFormParents(FlaskForm):
    
    # make a field for email
    email = StringField(
      'Email address',
      validators = [
          Email(),
          DataRequired()
      ]
    )

    # make a field for student id
    student_roll = StringField(
        'Student Roll',
        validators = [
            DataRequired()
        ]
    )

    # make a field for password
    password = PasswordField(
        'Password',
        validators = [ DataRequired() ]
    )

    login_button = SubmitField( 'Login' )