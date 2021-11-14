import os

class Config:
    SECRET_KEY='248fb9a5bdffa13c0bc136504ebf75c2'
    SQLALCHEMY_DATABASE_URI='mysql://root:@127.0.0.1/juniorschool'
#    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')