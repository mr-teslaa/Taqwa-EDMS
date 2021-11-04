#   importing  necessary module
from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from sqlalchemy.orm import backref, relationship

#   importing dataase
from main_app import db

#   importing login manager
from main_app import login_manager
from flask_login import UserMixin

#   making sure that the user is logged in
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    notice = db.relationship('Notice', backref='author', lazy=True)

    #   generating the password reseting roken
    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    #  verify the token if the token has exprired or invalid
    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Student(db.Model):
    student_roll = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(20), nullable = False)
    last_name = db.Column(db.String(20), nullable = False)
    father_name = db.Column(db.String(20), nullable = False)
    mother_name = db.Column(db.String(20), nullable = False)
    phone = db.Column(db.String(20), nullable = False)
    birth_cirtificate = db.Column(db.String(20), nullable = False)
    date_of_birth = db.Column(db.DateTime, nullable = False)
    address = db.Column(db.String(300), nullable = False)
    male = db.Column(db.Boolean)
    female = db.Column(db.Boolean)
    mail = db.Column(db.String(20), nullable = False)
    transportation = db.Column(db.Boolean, nullable = False)
    photo = db.Column(db.String(), nullable = False, default = 'default.jpg')
    signature = db.Column(db.String(), nullable = False, default = 'default.jpg')

    classroom_id = db.Column(db.Integer, db.ForeignKey('classroom.id'))

class Classroom(db.Model):
    id = db.Column(db.Integer, primary_key = True ,nullable = False)
    class_name = db.Column(db.String(), nullable = False)

class Parent(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20))
    username = db.Column(db.String(20))
    phone = db.Column(db.String(20))
    mail = db.Column(db.String(20))
    photo = db.Column(db.String(20), default = 'default.jpg')
    
    student_roll = db.Column(db.Integer, db.ForeignKey('student.student_roll'))
    



class Notice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"