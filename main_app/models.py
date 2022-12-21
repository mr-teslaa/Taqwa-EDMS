#   importing  necessary module
from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app

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


class Student(db.Model):
    __tablename__ = "student"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    classname = db.Column(db.String())
    roll = db.Column(db.String())
    address = db.Column(db.String())
    result = db.relationship('Result', backref='student_result', lazy=True)


class Result(db.Model):
    __tablename__ = "result"
    id = db.Column(db.Integer, primary_key=True)
    subjectname = db.Column(db.String())
    marks = db.Column(db.String())
    gpa = db.Column(db.String())
    grade = db.Column(db.String())
    exam_id = db.Column(db.Integer, db.ForeignKey('exam.id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)


class Exam(db.Model):
    __tablename__ = 'exam'
    id = db.Column(db.Integer, primary_key=True)
    exam_name = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    exam_subject = db.relationship('ExamSubject', backref='exam_subject', lazy=True)
    result = db.relationship('Result', backref='result', lazy=True)


class ExamSubject(db.Model):
    __tablename__ = 'exam_subject'
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(100), nullable=False)
    full_marks = db.Column(db.String(100), nullable=False)
    pass_marks = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    exam_id = db.Column(db.Integer, db.ForeignKey('exam.id'), nullable=False)