from flask import Blueprint
from flask import render_template

public_bp = Blueprint('public', __name__)

@public_bp.route('/')
def landing_page():
    return render_template('public/landing.html')