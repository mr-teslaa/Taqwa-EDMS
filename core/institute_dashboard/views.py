from flask import render_template, Blueprint,jsonify, request,url_for
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
    students = Student.query.all()
    return render_template('institute_dashboard/admission/admission-center.html' ,students=students)



@institute_dashboard_bp.route("/admission-center-data", methods=['POST'])
@institute_required
@login_required
def admission_center_data():
    # Get parameters from DataTables request
    start = int(request.form.get('start', 0))  # Start of the records for pagination
    length = int(request.form.get('length', 10))  # Number of records to return
    search_value = request.form.get('search[value]', '')  # Search query
    order_column = request.form.get('order[0][column]', 0)  # Column index for ordering
    order_dir = request.form.get('order[0][dir]', 'asc')  # Ordering direction (asc/desc)

    # Mapping columns to model fields
    columns = ['student_id', 'name_english', 'name_bangla', 'apply_class', 'marital_status']
    order_by = columns[int(order_column)]
    
    # Sorting direction
    if order_dir == 'desc':
        order_by = f'-{order_by}'
    
    # Base query for fetching student data
    query = Student.query
    
    # Apply search filter if there's a search query
    if search_value:
        query = query.filter(
            (Student.name_english.ilike(f'%{search_value}%')) |
            (Student.name_bangla.ilike(f'%{search_value}%')) |
            (Student.apply_class.ilike(f'%{search_value}%')) |
            (Student.marital_status.ilike(f'%{search_value}%'))
        )

    # Get total number of students after search
    total_filtered = query.count()
    
    # Apply ordering and pagination
    students = query.order_by(order_by).offset(start).limit(length).all()

    # Get total count of students without filtering
    total_students = Student.query.count()

    # Convert students to a list of dictionaries
    data = []
    for student in students:
        data.append({
            'student_id': student.student_id,
            'name_english': student.name_english,
            'name_bangla': student.name_bangla,
            'apply_class': student.apply_class,
            'marital_status': student.marital_status,
            'details': f'<a href="{url_for("institute_dashboard.student_details", student_id=student.student_id)}" class="btn btn-info btn-sm text-white">Details</a>'
        })

    # Return JSON response
    return jsonify({
        'draw': request.form.get('draw', 1),
        'recordsTotal': total_students,
        'recordsFiltered': total_filtered,
        'data': data
    })



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
