import os
from werkzeug.utils import secure_filename
import secrets
from flask import request, redirect, url_for, flash, render_template, Blueprint, current_app
from core import db
from core.models import Student, Application

admission_bp = Blueprint('admission', __name__)



def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']

def generate_random_filename(filename):
    # Generate a random hex string and append the file extension
    random_hex = secrets.token_hex(8)
    _, file_ext = os.path.splitext(filename)
    return f"{random_hex}{file_ext}"


@admission_bp.route('/student/admission', methods=['GET', 'POST'])
def student_admission():
    if request.method == 'POST':
        student_data = {
            "name_english": request.form.get('student_name_english'),
            "name_bangla": request.form.get('student_name_bangla'),
            "apply_class": request.form.get('apply_class'),
            "date_of_birth": request.form.get('date_of_birth'),
            "birth_certificate_no": request.form.get('birth_certificate'),
            "gender": request.form.get('gender'),
            "religion": request.form.get('religion'),
            "blood_group": request.form.get('blood_group'),
            "nationality": request.form.get('nationality'),
            "marital_status": request.form.get('marital_status'),
            "father_name_english": request.form.get('father_name_english'),
            "father_name_bangla": request.form.get('father_name_bangla'),
            "father_mobile": request.form.get('father_mobile'),
            "father_nid": request.form.get('father_nid'),
            "mother_name_english": request.form.get('mother_name_english'),
            "mother_name_bangla": request.form.get('mother_name_bangla'),
            "mother_mobile": request.form.get('mother_mobile'),
            "mother_nid": request.form.get('mother_nid'),
            "present_address": request.form.get('present_address'),
            "division": request.form.get('division'),
            "district": request.form.get('district'),
            "upazilla": request.form.get('upazilla'),
            "post_office": request.form.get('post_office'),
            "post_code": request.form.get('post_code'),
            "permanent_address": request.form.get('permanent_address'),
            "guardian_name": request.form.get('guardian_name'),
            "relationship": request.form.get('relationship'),
            "guardian_mobile": request.form.get('guardian_mobile'),
            "guardian_occupation": request.form.get('guardian_occupation'),
            "prev_institute_name": request.form.get('institute'),
            "prev_institute_address": request.form.get('institute_address'),
            "prev_passing_year": request.form.get('year'),
            "prev_roll": request.form.get('roll'),
            "prev_class": request.form.get('class'),
            "photo": None
        }

        # Handle the photo upload
        photo = request.files.get('photo')
        if photo and allowed_file(photo.filename):
            original_filename = secure_filename(photo.filename)
            new_filename = generate_random_filename(original_filename)
            file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], new_filename)
            photo.save(file_path)
            student_data["photo"] = new_filename  # Save the new filename in your data

        print('Student data: ')
        print(student_data)
        new_student = Student(**student_data)
        db.session.add(new_student)
        db.session.commit()

        new_application = Application(student_id=new_student.id)
        db.session.add(new_application)
        db.session.commit()

        flash('Application submitted successfully!', 'success')
        return redirect(url_for('admission.student_admission'))

    return render_template('admission/admission-form.html')
