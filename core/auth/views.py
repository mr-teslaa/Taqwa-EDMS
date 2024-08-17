from flask import Blueprint
from flask import render_template

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login')
def login():
    return render_template('auth/login.html')

@auth_bp.route('/register/institute')
def register_institute():
    return 'register institute page'