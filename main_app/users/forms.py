from enum import unique
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import PasswordField
from wtforms import SubmitField
from wtforms import SelectField
from wtforms import BooleanField
from wtforms import IntegerField

from flask_wtf.file import FileField
from flask_wtf.file import FileAllowed
from wtforms.fields.core import DateField
from wtforms.fields.core import RadioField

#   wtf validators
from wtforms.validators import DataRequired
from wtforms.validators import Length
from wtforms.validators import Email
from wtforms.validators import EqualTo




class AdmissionForm(FlaskForm):

    unique_id = StringField(
        'Unique ID',
        validators = [DataRequired()]
    )

    roll_id = StringField(
        'Roll ID',
        validators = [DataRequired()]
    )

    #   make a field for first name
    firstname = StringField(
        'First name',
        validators = [ DataRequired() ]
    )

    #   make a field for last name
    lastname = StringField(
        'Last name',
        validators = [ DataRequired() ]
    )

    #   make field for father's name
    father_name = StringField(
        'Father\'s Name',
        validators = [ DataRequired() ]
    )

    #   make a field for mother's name
    mother_name = StringField(
        'Mother\'s Name',
        validators = [ DataRequired() ]
    )

    #   make select field for select admitted class
    applicable_class = SelectField(
        'Class you want to apply',
        choices = [
            ('n/a', '--- Select Class ---'),
            ('play', 'PLAY'),
            ('nursary', 'NURSARY'),
            ('one', 'ONE'),
            ('two', 'TWO'),
            ('three', 'THREE'),
            ('four', 'FOUR'),
            ('two', 'FIVE'),
            ('three', 'SIX'),
            ('one', 'SEVEN'),
            ('two', 'EIGHT')
        ]
    )

    #   make a field for phone number
    phone_number = StringField(
        'Phone Number',
        validators = [
            DataRequired()
        ]
    )

    #   make a datetime field for date of birth
    #   want to make this a DateTimeField. But do not know actual syntax
    birth_date = StringField(
        'Date of Birth',
        validators = [
            DataRequired()
        ]
    )

    #   make a text field for birth cirtificate id
    birth_cirtificate_no  = IntegerField(
        'Birth Cirtificate No',
        validators = [
            DataRequired()
        ]
    )

    #   gender selection
    gender = SelectField(
        'Gender',
        choices = [
            ('n/a', '--- Select Gender ---'),
            ('male', 'MALE'),
            ('female', 'FEMALE')
        ]
    )

    # transportation selection
    transportation_status = SelectField(
        'Transportation Status',
        choices = [
            ('n/a', '--- Select Transportation Status ---'),
            ('yes', 'YES'),
            ('no', 'NO')
        ]
    )

    #   make a field for care of address
    care_of = StringField(
        'Care of',
        validators = [ DataRequired() ]
    )

    #   make a field for zip code
    zip_code = IntegerField(
        'Post Code',
        validators = [ DataRequired() ]
    )

    #   make a filed for address
    address = StringField(
        'Address',
        validators = [ DataRequired() ]
    )

    #   make a field for email
    email = StringField(
        'E-mail',
        validators = [
            Email(),
            DataRequired()
        ]
    )

    #   make a photo upload field
    photo = FileField(
        'Photo',
        validators = [ 
            DataRequired() , 
            FileAllowed(['jpg', 'jpeg', 'png'])
        ]
    )

    #   make a field for signature
    signature = FileField(
        'Signature',
        validators = [ 
            DataRequired(), 
            FileAllowed(['jpg', 'jpeg', 'png'])]
    )

    #  make a date of birth field
    birth_date = DateField('Date of Birth', format = '%d-%m-%Y')

    
    #   make a submit field
    submit = SubmitField('Submit')










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









class ApplyTeacherForm(FlaskForm):

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

    #   make field for c.v
    cv = FileField(
        'Curriculam Vita',
        validators = [ DataRequired() ]
    )

    #   make filed for photo
    photo = FileField(
        'Photo',
        validators = [ DataRequired() ]
    )

    #   make field for signature
    signature = FileField(
        'Signature',
        validators = [ DataRequired() ]
    )

    #   make a submit buton
    submit = SubmitField( 'Submit' )









class LoginForm(FlaskForm):

    #   make a field for username
    email = StringField(
        'E-mail',
        validators = [
            DataRequired(),
            Email()
        ]
    )

    #   make a field for password
    password = PasswordField(
        'Password',
        validators = [ DataRequired() ]
    )

    #   makea a checkbox for remember me
    remember_me = BooleanField( 'Remember me' )

    #   make a login buton
    login_button = SubmitField( 'Login' )









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
    student_id = StringField(
        'Student ID',
        validators = [
            DataRequired(),
            Length(7, 7)
        ]
    )

    # make a field for password
    password = PasswordField(
        'Password',
        validators = [ DataRequired() ]
    )

    login_button = SubmitField( 'Login' )



class DemoRegForm(FlaskForm):
    #   make username for teacher
    username = StringField(
        'Username',
        validators = [ DataRequired() ]
    )

    # make a field for email
    email = StringField(
      'Email address',
      validators = [
          Email(),
          DataRequired()
      ]
    )

    # make a field for password
    password = PasswordField(
        'Password',
        validators = [ DataRequired() ]
    )

    #   make cofirm password
    confirm_password = PasswordField(
        'Confirm Password',
        validators = [
            DataRequired(),
            EqualTo('password')
        ]
    )

    reg_button = SubmitField( 'Register' )
