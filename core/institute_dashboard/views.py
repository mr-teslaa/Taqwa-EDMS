from flask import request, redirect, url_for, flash, render_template, Blueprint, current_app


institute_dashboard_bp = Blueprint('institute_dashboard', __name__)

@institute_dashboard_bp.route('/admin')
def institute_dashboard():
    return render_template('institute_dashboard/institute_dashboard.html')