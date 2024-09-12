from functools import wraps
from flask import redirect, url_for,abort
from flask_login import current_user
from core.models import Institute

def institute_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not isinstance(current_user, Institute):
            abort(403)
        return f(*args, **kwargs)
    return decorated_function