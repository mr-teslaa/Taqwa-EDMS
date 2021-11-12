from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SubmitField
from wtforms import SelectField
from wtforms import BooleanField
from wtforms import IntegerField
from wtforms import FileField
from flask_wtf.file import FileAllowed
from wtforms.fields.core import DateField
from wtforms.fields.simple import PasswordField

#   wtf validators
from wtforms.validators import DataRequired, EqualTo
from wtforms.validators import Length
from wtforms.validators import Email



class AdmissionForm(FlaskForm):
    
    #   make a field for first name
    firstname = StringField(
        'First name',
        validators = [
            DataRequired(),
            Length(min=3, max=50)
        ]
    )

    #   make a field for last name
    lastname = StringField(
        'Last name',
        validators = [
            DataRequired(),
            Length(min=3, max=50)
        ]
    )

    #   make field for father's name
    father_name = StringField(
        'Father\'s Name',
        validators = [
            DataRequired(),
            Length(min=3, max=50)
        ]
    )

    #   make a field for mother's name
    mother_name = StringField(
        'Mother\'s Name',
        validators = [
            DataRequired(),
            Length(min=3, max=50)
        ]
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
            DataRequired(),
            Length(11, 13)
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

    #   make a radio for male
    male = BooleanField('Male')

    #   make a radio for female
    female = BooleanField('Female')

    #   make a radio for trasportation yes
    yes = BooleanField('Yes')

    #   make a radio for trasportation no
    no = BooleanField('no')

    #   make a filed for address
    address = StringField(
        'Address',
        validators = [
            DataRequired(),
            Length(min=3, max=20)
        ]
    )

    #   make a field for email
    email = StringField(
        'E-mail',
        validators = [
            Email(),
            DataRequired()
        ]
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
            validators=[
                DataRequired()
            ]
    )

    #   make a photo upload field
    photo = FileField(
        'Photo',
        validators = [ DataRequired() , FileAllowed(['jpg', 'jpeg', 'png'])]
    )

    #   make a field for signature
    signature = FileField(
        'Signature',
        validators = [ DataRequired(), FileAllowed(['jpg', 'jpeg', 'png'])]
    )

    #  make a date of birth field
    birth_date = DateField('Date of Birth', format = '%d-%m-%Y')

    
    #   make a submit field
    submit = SubmitField('Submit')
