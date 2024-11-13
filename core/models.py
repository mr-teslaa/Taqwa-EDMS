from datetime import datetime
from flask import current_app
from itsdangerous import URLSafeTimedSerializer as Serializer
from core import db,login_manager
from flask_login import UserMixin
from core import bcrypt

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    photo = db.Column(db.String(20), nullable=False, default="default-photo.jpg")
    signature = db.Column(
        db.String(20), nullable=False, default="default-signature.jpg"
    )
    password = db.Column(db.String(60), nullable=False)
    institute_name = db.Column(db.String(60), nullable=False)
    institute_unique_id = db.Column(db.String(60), nullable=False)
    eiin_id = db.Column(db.String(60))
    institute_address = db.Column(db.String(60), nullable=False)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config["SECRET_KEY"])
        return s.dumps({"user_id": self.id}, salt="password-reset-salt")

    @staticmethod
    def verify_reset_token(token, expires_sec=1800):
        s = Serializer(current_app.config["SECRET_KEY"])
        try:
            user_id = s.loads(token, salt="password-reset-salt", max_age=expires_sec)[
                "user_id"
            ]
        except Exception:
            return None
        return User.query.get(user_id)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(20), unique=True, nullable=False)
    application_number = db.Column(db.String(20), unique=True, nullable=False)
    name_english = db.Column(db.String(100), nullable=False)
    name_bangla = db.Column(db.String(100))
    apply_class = db.Column(db.String(20), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    birth_certificate_no = db.Column(db.String(20), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    religion = db.Column(db.String(20))
    blood_group = db.Column(db.String(5))
    nationality = db.Column(db.String(50), nullable=False)
    marital_status = db.Column(db.String(10))
    father_name_english = db.Column(db.String(100), nullable=False)
    father_name_bangla = db.Column(db.String(100))
    father_mobile = db.Column(db.String(20), nullable=False)
    father_nid = db.Column(db.String(20))
    mother_name_english = db.Column(db.String(100), nullable=False)
    mother_name_bangla = db.Column(db.String(100))
    mother_mobile = db.Column(db.String(20), nullable=False)
    mother_nid = db.Column(db.String(20))
    present_address = db.Column(db.Text, nullable=False)
    present_division = db.Column(db.String(50), nullable=False)
    present_district = db.Column(db.String(50), nullable=False)
    present_upazilla = db.Column(db.String(50), nullable=False)
    present_post_office = db.Column(db.String(50), nullable=False)
    present_post_code = db.Column(db.String(10), nullable=False)
    permanent_address = db.Column(db.Text)
    permanent_division = db.Column(db.String(50), nullable=False)
    permanent_district = db.Column(db.String(50), nullable=False)
    permanent_upazilla = db.Column(db.String(50), nullable=False)
    permanent_post_office = db.Column(db.String(50), nullable=False)
    permanent_post_code = db.Column(db.String(10), nullable=False)
    guardian_name = db.Column(db.String(100))
    relationship = db.Column(db.String(50))
    guardian_mobile = db.Column(db.String(20))
    guardian_occupation = db.Column(db.String(50))
    prev_institute_name = db.Column(db.String(100))
    prev_institute_address = db.Column(db.String(100))
    prev_passing_year = db.Column(db.String(4))
    prev_roll = db.Column(db.String(20))
    prev_class = db.Column(db.String(20))
    photo = db.Column(db.String(100))

    def __init__(self, **kwargs):
        super(Student, self).__init__(**kwargs)
        self.student_id = self.generate_unique_id()
        self.application_number = self.generate_application_number()

    def generate_unique_id(self):
        return f"ST-{int(datetime.utcnow().timestamp())}"

    def generate_application_number(self):
        return f"APP-{int(datetime.utcnow().timestamp())}"


class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"), nullable=False)
    status = db.Column(db.String(20), nullable=False, default="Pending")
    submission_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    student = db.relationship("Student", backref=db.backref("applications", lazy=True))


@login_manager.user_loader
def load_user(user_id):
    return Institute.query.get(int(user_id))

class Institute(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)