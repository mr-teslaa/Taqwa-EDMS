from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, DateField, FileField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Optional

class StudentAdmissionForm(FlaskForm):
    # students info
    student_name_english = StringField('Student Name (English)', validators=[DataRequired(), Length(max=200)])
    student_name_bangla = StringField('Student Name (বাংলা)', validators=[DataRequired(), Length(max=200)])
    apply_class = SelectField('Apply for class', choices=[
        ('', '--- Select Class ---'), 
        ('play', 'Play'), 
        ('nursary', 'Nursary'), 
        ('one', 'One'), 
        ('two', 'Two'), 
        ('three', 'Three'), 
        ('four', 'Four'), 
        ('five', 'Five'), 
        ('six', 'Six'), 
        ('seven', 'Seven'), 
        ('eight', 'Eight'), 
        ('nine', 'Nine'), 
        ('ten', 'Ten')
    ], validators=[DataRequired()])
    date_of_birth = DateField('Date Of Birth', format='%Y-%m-%d', validators=[DataRequired()])
    birth_certificate_no = StringField('Birth Certificate No', validators=[DataRequired(), Length(max=20)])
    gender = SelectField('Gender', choices=[
        ('', '--- Select Gender ---'),
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], validators=[DataRequired()])
    religion = SelectField('Religion', choices=[
        ('', 'Choose...'),
        ('islam', 'Islam'),
        ('sonaton', 'Sonaton'),
        ('christian', 'Christian'),
        ('buddhism', 'Buddhism')
    ], validators=[DataRequired()])
    blood_group = SelectField('Blood Group', choices=[
        ('', 'Choose...'),
        ('A+', 'A +(ve)'),
        ('A-', 'A -(ve)'),
        ('B+', 'B +(ve)'),
        ('B-', 'B -(ve)'),
        ('O+', 'O +(ve)'),
        ('AB+', 'AB + (ve)'),
        ('AB-', 'AB -(ve)')
    ], validators=[DataRequired()])
    nationality = StringField('Nationality', validators=[DataRequired(), Length(max=50)])
    marital_status = SelectField('Marital status', choices=[
        ('', '--- Select One ---'),
        ('married', 'Married'),
        ('unmarried', 'Unmarried')
    ], validators=[DataRequired()])
    # father info
    father_name_english = StringField('Father Name (English)', validators=[DataRequired(), Length(max=100)])
    father_name_bangla = StringField('Father Name (বাংলা)', validators=[DataRequired(), Length(max=100)])
    father_mobile = StringField('Father Mobile No', validators=[DataRequired(), Length(max=15)])
    father_nid = StringField('Father NID/Passport', validators=[DataRequired(), Length(max=20)])
    # mother info 
    mother_name_english = StringField('Mother Name (English)', validators=[DataRequired(), Length(max=100)])
    mother_name_bangla = StringField('Mother Name (বাংলা)', validators=[DataRequired(), Length(max=100)])
    mother_mobile = StringField('Mother Mobile No', validators=[DataRequired(), Length(max=15)])
    mother_nid = StringField('Mother NID/Passport', validators=[DataRequired(), Length(max=20)])
    # student present address 
    present_address = TextAreaField('Present Address', validators=[DataRequired()])
    present_division = StringField('Present Division', validators=[DataRequired(), Length(max=50)])
    present_district = StringField('Present District/Zilla', validators=[DataRequired(), Length(max=50)])
    present_upazilla = StringField('Present Upazilla', validators=[DataRequired(), Length(max=50)])
    present_post_office = StringField('Present Post Office', validators=[DataRequired(), Length(max=50)])
    present_post_code = StringField('Present Post Code', validators=[DataRequired(), Length(max=10)])
    # student permanent address 
    permanent_address = TextAreaField('Permanent Address', validators=[DataRequired()])
    permanent_division = StringField('Permanent Division', validators=[DataRequired(), Length(max=50)])
    permanent_district = StringField('Permanent District/Zilla', validators=[DataRequired(), Length(max=50)])
    permanent_upazilla = StringField('Permanent Upazilla', validators=[DataRequired(), Length(max=50)])
    permanent_post_office = StringField('Permanent Post Office', validators=[DataRequired(), Length(max=50)])
    permanent_post_code = StringField('Permanent Post Code', validators=[DataRequired(), Length(max=10)])
    # guardian info
    guardian_name = StringField('Guardian Name', validators=[DataRequired(), Length(max=100)])
    relationship = StringField('Relationship', validators=[DataRequired(), Length(max=50)])
    guardian_mobile = StringField('Guardian Mobile', validators=[DataRequired(), Length(max=15)])
    guardian_occupation = StringField('Occupation', validators=[DataRequired(), Length(max=50)])
    # previous institute data 
    prev_institute_name = StringField('Previous Institute Name', validators=[Optional(), Length(max=100)])
    prev_institute_address = StringField('Previous Institute Address', validators=[Optional(), Length(max=100)])
    prev_passing_year = StringField('Previous Passing Year', validators=[Optional(), Length(max=4)])
    prev_roll = StringField('Previous Roll', validators=[Optional(), Length(max=20)])
    prev_class = StringField('Previous Class', validators=[Optional(), Length(max=20)])
    # photo and agreement of terms 
    photo = FileField('Photo', validators=[DataRequired()])
    agree_tos = BooleanField('Agree with Terms of Service and Privacy Policy', validators=[DataRequired()])
    
    submit = SubmitField('Apply For Admission')
