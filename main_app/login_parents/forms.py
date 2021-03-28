from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
       
#   wtf validators
from wtforms.validators import DataRequired, Length, Email


# make a login form for parents
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

