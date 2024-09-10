from flask import render_template, Blueprint, request
from flask_paginate import Pagination, get_page_parameter
from core.models import Student

institute_dashboard_bp = Blueprint("institute_dashboard", __name__)


@institute_dashboard_bp.route("/institute_dashboard")
def institute_dashboard():
    students = Student.query.all()
    num_students = Student.query.count()
    male_students = Student.query.filter_by(gender="male").count()
    female_students = Student.query.filter_by(gender="female").count()
    return render_template(
        "institute_dashboard/institute_dashboard.html",
        students=students,
        num_students=num_students,
        male_students=male_students,
        female_students=female_students,
    )


@institute_dashboard_bp.route("/student/<student_id>")
def student_details(student_id):
    student = Student.query.filter_by(student_id=student_id).first_or_404()
    return render_template("institute_dashboard/student_details.html", student=student)
