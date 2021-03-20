from flask  import Blueprint, render_template
from .forms import LoginFormParents

login_parents_bp = Blueprint("login_parents_bp", __name__, 
    template_folder= "templates",
    static_folder  = "static")

#   login as parents route
@login_parents_bp.route("/parents/login", methods=["GET", "POST"])
def loginParents():
    form = LoginFormParents()
    return render_template('login_parents.html', form=form)
