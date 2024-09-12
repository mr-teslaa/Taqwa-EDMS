import os
from werkzeug.utils import secure_filename
import secrets
from flask import request, redirect, url_for, flash, render_template, Blueprint, current_app
from core import db
from core.models import Student, Application
from core.admission.forms import StudentAdmissionForm
from core.utils.save_file import save_file, allowed_file
admission_bp = Blueprint('admission', __name__)


@admission_bp.route('/', methods=['GET', 'POST'])
def student_admission():
    form = StudentAdmissionForm()

    if request.method == 'POST' and form.validate_on_submit():
        student_data = {
            "name_english": form.student_name_english.data,
            "name_bangla": form.student_name_bangla.data,
            "apply_class": form.apply_class.data,
            "date_of_birth": form.date_of_birth.data,
            "birth_certificate_no": form.birth_certificate_no.data,
            "gender": form.gender.data,
            "religion": form.religion.data,
            "blood_group": form.blood_group.data,
            "nationality": form.nationality.data,
            "marital_status": form.marital_status.data,
            "father_name_english": form.father_name_english.data,
            "father_name_bangla": form.father_name_bangla.data,
            "father_mobile": form.father_mobile.data,
            "father_nid": form.father_nid.data,
            "mother_name_english": form.mother_name_english.data,
            "mother_name_bangla": form.mother_name_bangla.data,
            "mother_mobile": form.mother_mobile.data,
            "mother_nid": form.mother_nid.data,
            "present_address": form.present_address.data,
            "present_division": form.present_division.data,
            "present_district": form.present_district.data,
            "present_upazilla": form.present_upazilla.data,
            "present_post_office": form.present_post_office.data,
            "present_post_code": form.present_post_code.data,
            "permanent_address": form.permanent_address.data,
            "permanent_division": form.permanent_division.data,
            "permanent_district": form.permanent_district.data,
            "permanent_upazilla": form.permanent_upazilla.data,
            "permanent_post_office": form.permanent_post_office.data,
            "permanent_post_code": form.permanent_post_code.data,
            "guardian_name": form.guardian_name.data,
            "relationship": form.relationship.data,
            "guardian_mobile": form.guardian_mobile.data,
            "guardian_occupation": form.guardian_occupation.data,
            "prev_institute_name": form.prev_institute_name.data,
            "prev_institute_address": form.prev_institute_address.data,
            "prev_passing_year": form.prev_passing_year.data,
            "prev_roll": form.prev_roll.data,
            "prev_class": form.prev_class.data,
            "photo": None
        }

        # Handle the photo upload
        if form.photo.data:
            photo = form.photo.data
            if allowed_file(photo.filename):
                file_path = save_file(photo)
                new_filename = os.path.basename(file_path)
                student_data["photo"] = new_filename

        print('Student data: ')
        print(student_data)
        new_student = Student(**student_data)
        db.session.add(new_student)
        db.session.commit()

        new_application = Application(student_id=new_student.id)
        db.session.add(new_application)
        db.session.commit()

        flash('Application submitted successfully!', 'success')
        return redirect(url_for('public.landing_page'))
    
    elif request.method == 'POST':
        
        flash('Please fill in all required fields.','danger')


    return render_template('admission/admission.html', form=form)
