from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
       
#   wtf validators
from wtforms.validators import DataRequired, Length, Email


# make a Login form
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
