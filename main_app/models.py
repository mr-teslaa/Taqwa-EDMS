from flask import current_app as app
from flask_sqlalchemy import SQLAlchemy
# import datetime module 
# from datetime import datetime

# from main_app import db

db = SQLAlchemy()

# make a class for user in database model
class Users(db.Model):
    __tablename__ = "users"
    id            = db.Column(db.Integer,     primary_key=True)
    username      = db.Column(db.String(20),  unique=True, nullable=False)
    email         = db.Column(db.String(120), unique=True, nullable=False)
    password      = db.Column(db.String(),    nullable=False)
    image_file    = db.Column(db.String(20),  nullable=False)

class User_Type(db.Model):
    __tablename__ = "user_type"
    id_user_type  = db.Column(db.Integer,    primary_key=True)
    name          = db.Column(db.String(20), unique=True, nullable=False)
    desc          = db.Column(db.String(20), unique=True, nullable=False)

class Students(db.Model):
    __tablename__ = "students"
    id_student           = db.Column(db.Integer,    primary_key=True)
    user_id              = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    father_name          = db.Column(db.String(20), unique=True, nullable=False)
    mother_name          = db.Column(db.String(20), unique=True, nullable=False)
    phone_number         = db.Column(db.String(20), unique=True, nullable=False)
    birth_certificate_no = db.Column(db.Integer, nullable=False)
    date_of_admition     = db.Column(db.DateTime, nullable=False)

class Notice(db.Model):
    __tablename__ = "notice"
    id_title          = db.Column(db.Integer,    primary_key=True)
    title             = db.Column(db.String(20), unique=True, nullable=False)
    description       = db.Column(db.String(20), unique=True, nullable=False)
    image             = db.Column(db.String(20), unique=True)
    date_of_post      = db.Column(db.DateTime, nullable=False)
    post_by           = db.Column(db.Integer, nullable=False)

class Fees(db.Model):
    __tablename__ = "fees"
    id_fee            = db.Column(db.Integer, primary_key=True)
    user_id           = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    tuition_fee       = db.Column(db.Integer, nullable=False)
    transport_fee     = db.Column(db.Integer, nullable=False)
    total_monthly_fee = db.Column(db.Integer, nullable=False)

class Address(db.Model):
    __tablename__ = "address"
    id_address        = db.Column(db.Integer, primary_key=True)
    street            = db.Column(db.String(20), unique=True, nullable=False)
    district          = db.Column(db.String(20), unique=True, nullable=False)
    post_office       = db.Column(db.String(20), unique=True, nullable=False)
    user_id           = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
