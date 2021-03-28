from flask  import Blueprint, render_template
from .forms import ApplyParentsForm

apply_parents_bp = Blueprint("apply_parents_bp", __name__, 
    template_folder= "templates",
    static_folder  = "static")

#   login as parents route
@apply_parents_bp.route("/parents/apply", methods=["GET", "POST"])
def apply_parents():
    form = ApplyParentsForm()
    return render_template('apply_parents.html', form=form)
