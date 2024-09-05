import os

class Config:
    SECRET_KEY='248fb9a5bdffa13c0bc136504ebf75c2'
    # SQLALCHEMY_DATABASE_URI='sqlite:///taqwaems.db'
    
    # =======FOR TEST WITH XAMPP LOCAL SERVER ===========
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/taqwaems'
    
    # CREATE PATH FOR UPLOAD
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static', 'uploads') 
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'} 
    # Ensure the upload folder exists
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    # SITE NAME
    SITE_TITLE = 'TAQWA EMS'

    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    # MAIL_SERVER = 'smtp.gmail.com'
    # MAIL_PORT = 587
    # MAIL_USE_TLS = True
    # MAIL_USERNAME = os.environ.get('EMAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')