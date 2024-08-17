from flask import Blueprint

admin_dashboard_bp = Blueprint('admin_dashboard', __name__)

@admin_dashboard_bp.route('/')
def admin_dashboard():
    return 'dashboard page'