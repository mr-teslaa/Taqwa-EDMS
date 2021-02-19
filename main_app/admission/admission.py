from flask  import Blueprint, render_template
from .forms import AdmissionForm

admission_bp = Blueprint("admission_bp", __name__, 
    template_folder= "templates",
    static_folder  = "static")

#   login as parents route
@admission_bp.route("/admission", methods=["GET", "POST"])
def admission():
    form = AdmissionForm()
    return render_template('admission.html', form=form)
