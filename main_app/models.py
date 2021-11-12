#   importing  necessary module
from datetime import datetime
from enum import unique
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from sqlalchemy.ext.declarative import declared_attr


#   importing database
from main_app import db

#   importing login manager
from main_app import login_manager
from flask_login import UserMixin

#   -- multiple user log-in process, User_Class = [Student, Parent...] models --
#   making sure that the user is logged in
@login_manager.user_loader
def load_user(user_id, User_Class):
    return User_Class.query.get(int(user_id))


class AbstractUser(db.Model, UserMixin):

    #model inheritence using flask-sqlalchemy
    __abstract__ = True
    
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    email = db.Column(db.String(120), unique=True)
    phone = db.Column(db.String(20))
    image_file = db.Column(db.String(20), default='default.jpg')
    password = db.Column(db.String(60))

    #Foreign key practice in abstract classes
    @declared_attr
    def role_id(cls):
       return db.Column(db.Integer, db.ForeignKey('roles.id'))
    

#Inherited AbstractUser
class Student(AbstractUser):
    student_roll= db.Column(db.Integer, primary_key = True)
    father_name = db.Column(db.String(20), nullable = False)
    mother_name = db.Column(db.String(20), nullable = False)
    birth_cirtificate = db.Column(db.String(20), nullable = False)
    date_of_birth = db.Column(db.DateTime, nullable = False)
    address = db.Column(db.String(300), nullable = False)
    male = db.Column(db.Boolean)
    female = db.Column(db.Boolean)
    transportation = db.Column(db.Boolean, nullable = False)
    signature = db.Column(db.String(), nullable = False, default = 'default.jpg')

    classroom_id = db.Column(db.Integer, db.ForeignKey('classroom.id'))

#Inherited AbstractUser
class Parent(AbstractUser):
    id = db.Column(db.Integer, primary_key = True)
    student_roll = db.Column(db.Integer, db.ForeignKey('student.student_roll'))

class Classroom(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    class_name = db.Column(db.String(), nullable = False)

class Roles(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    role = db.Column(db.String(), nullable = False)

#Temp. Invalid
class Notice():
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
