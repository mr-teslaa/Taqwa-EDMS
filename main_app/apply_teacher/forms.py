from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FileField, PasswordField
       
#   wtf validators
from wtforms.validators import DataRequired, Email, EqualTo

#   make a Apply Form for Teacher
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
