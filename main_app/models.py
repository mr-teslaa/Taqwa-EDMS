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


# table for all notice
class Notice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    status = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


# table for student's info
class StudentsInfo(db.Model):
    __tablename__ = 'students_info'
    unique_id = db.Column(db.String(20), unique=True, primary_key=True)
    roll_id = db.Column(db.Integer, nullable=False)
    firstname = db.Column(db.String(200))
    lastname = db.Column(db.String(200))
    father_name = db.Column(db.String(200))
    mother_name = db.Column(db.String(200))
    current_class = db.Column(db.String(20))
    phone_number = db.Column(db.String(11))
    birth_cirtificate_no = db.Column(db.String(20), unique=True)
    birth_date = db.Column(db.String(50))
    gender = db.Column(db.String(20))
    care_of = db.Column(db.String(300))
    zip_code = db.Column(db.String(10))
    address = db.Column(db.String(500))
    email = db.Column(db.String(100))
    image_file = db.Column(db.String(20), default='default.jpg')
    signature = db.Column(db.String(20))
    transportation_status = db.Column(db.String(5), default='no')
    graduation_status = db.Column(db.String(100), default='no')
    

    def __repr__(self):
        return f"User('{self.uniqueID}', '{self.firstname}', '{self.lastname}', '{self.father_name}', '{self.mother_name}', '{self.current_class}', '{self.phone_number}', '{self.birth_cirtificate_no}', '{self.birth_date}', '{self.gender}', '{self.care_of}', '{self.zip_code}', '{self.address}', '{self.email}', '{self.image_file}', '{self.signature}', '{self.transportation_status}', '{self.graduation_status}')"


# table for total 100 marks
class Marks(db.Model):
    __tablename__ = 'marks'
    id = db.Column(db.Integer, primary_key=True)
    unique_id = db.Column(db.String(500), db.ForeignKey('students_info.unique_id'))
    roll_id = db.Column(db.String(500), db.ForeignKey('students_info.roll_id'))
    classname = db.Column(db.String(120), nullable=False)
    name = db.Column(db.String(300), nullable=False)
    bengali = db.Column(db.String(100), nullable=False)
    bengali2 = db.Column(db.String(100), nullable=False)
    english = db.Column(db.String(100), nullable=False)
    english2 = db.Column(db.String(100), nullable=False)
    mathematics = db.Column(db.String(100), nullable=False)
    science = db.Column(db.String(100), nullable=False)
    bandg = db.Column(db.String(100), nullable=False)
    religion = db.Column(db.String(100), nullable=False)
    total = db.Column(db.String(800), nullable=False)

    def __repr__(self):
        return f"Marks('{self.roll_id}', '{self.classname}', '{self.name}', '{self.bengali}', '{self.bengali2}', '{self.english}', '{self.english2}', '{self.mathematics}', '{self.science}', '{self.bandg}', '{self.religion}')"


# table for total 50 marks
class Marks50(db.Model):
    __tablename__ = 'marks50'
    id = db.Column(db.Integer, primary_key=True)
    unique_id = db.Column(db.String(500), db.ForeignKey('students_info.unique_id'))
    roll_id = db.Column(db.String(500), db.ForeignKey('students_info.roll_id'))
    classname = db.Column(db.String(120))
    name = db.Column(db.String(300))
    bengali = db.Column(db.String(100))
    english = db.Column(db.String(100))
    mathematics = db.Column(db.String(100))
    science = db.Column(db.String(100))
    bandg = db.Column(db.String(100))
    religion = db.Column(db.String(100))
    gpa = db.Column(db.String(800))
    grade = db.Column(db.String(800))
    total = db.Column(db.String(800))
    examname = db.Column(db.String(100))
    examyear = db.Column(db.String(100))

    def __repr__(self):
        return f"Marks50('{self.roll_id}', '{self.classname}', '{self.name}', '{self.bengali}', '{self.english}', '{self.mathematics}', '{self.science}', '{self.bandg}', '{self.religion}', '{self.gpa}', '{self.grade}', '{self.total}', '{self.examname }', '{self.examyear}')"