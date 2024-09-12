from flask import render_template, Blueprint
from core.models import Student
from core.utils.decorators import institute_required
from flask_login import login_required


institute_dashboard_bp = Blueprint("institute_dashboard", __name__)


# INSTITUTE DASHBOARD
@institute_dashboard_bp.route("/dashboard")
@institute_required
@login_required
def institute_dashboard():
    students = Student.query.all()
    total_student = Student.query.count()
    total_male_student = Student.query.filter_by(gender="male").count()
    total_female_student = Student.query.filter_by(gender="female").count()
    return render_template(
        "institute_dashboard/institute_dashboard.html",
        students=students,
        total_student=total_student,
        total_male_student=total_male_student,
        total_female_student=total_female_student,
    )

# ADMISSION CENTER
@institute_dashboard_bp.route("/admission-center")
@institute_required
@login_required
def admission_center():
    return render_template('institute_dashboard/admission/admission-center.html')


# ALL STUDENT LIST PAGE
@institute_dashboard_bp.route("/students")
@institute_required
@login_required
def students():
    return render_template('institute_dashboard/students/students.html')


# INDIVIDUAL STUDENT DETAILS PAGE
@institute_dashboard_bp.route("/student/<student_id>")
@institute_required
@login_required
def student_details(student_id):
    student = Student.query.filter_by(student_id=student_id).first_or_404()
    return render_template("institute_dashboard/students/student_details.html", student=student)
