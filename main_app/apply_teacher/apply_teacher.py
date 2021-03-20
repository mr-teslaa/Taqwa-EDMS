from flask  import Blueprint, render_template
from .forms import ApplyTeacherForm

apply_teacher_bp = Blueprint("apply_teacher_bp", __name__, 
    template_folder= "templates",
    static_folder  = "static")

#   login as parents route
@apply_teacher_bp.route("/teacher/apply", methods=["GET", "POST"])
def apply_teacher():
    form = ApplyTeacherForm()
    return render_template('apply_teacher.html', form=form)
