from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateField, TextAreaField, FileField
from wtforms.validators import DataRequired, Optional, Length, Regexp

class StudentAdmissionForm(FlaskForm):
    # Student Information
    student_name_english = StringField('Student Name (English)', validators=[DataRequired()])
    student_name_bangla = StringField('Student Name (বাংলা)', validators=[DataRequired()])
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
        ('ten', 'Ten'),
    ], validators=[DataRequired()])
    date_of_birth = DateField('Date of Birth', format='%Y-%m-%d', validators=[DataRequired()])
    birth_certificate = StringField('Birth Certificate No', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[
        ('', '--- Select Gender ---'),
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], validators=[DataRequired()])
    religion = SelectField('Religion', choices=[
        ('', 'Choose...'),
        ('islam', 'Islam'),
        ('sonaton', 'Sonaton'),
        ('christian', 'Christian'),
        ('buddhism', 'Buddhism'),
    ], validators=[DataRequired()])
    blood_group = SelectField('Blood Group', choices=[
        ('', 'Choose...'),
        ('a+', 'A +(ve)'),
        ('a-', 'A -(ve)'),
        ('b+', 'B +(ve)'),
        ('b-', 'B -(ve)'),
        ('o+', 'O +(ve)'),
        ('ab+', 'AB +(ve)'),
        ('ab-', 'AB -(ve)'),
    ], validators=[DataRequired()])
    nationality = StringField('Nationality', validators=[DataRequired()])
    marital_status = SelectField('Marital Status', choices=[
        ('', '--- Select One ---'),
        ('married', 'Married'),
        ('unmarried', 'Unmarried'),
    ], validators=[DataRequired()])

    # Parent's Information
    father_name_english = StringField('Father Name (English)', validators=[DataRequired()])
    father_name_bangla = StringField('Father Name (বাংলা)', validators=[DataRequired()])
    father_mobile = StringField('Father Mobile No', validators=[
        DataRequired(), Regexp(r'^\d{10,15}$', message="Invalid mobile number")])
    father_nid = StringField('Father NID/Passport', validators=[DataRequired()])

    mother_name_english = StringField('Mother Name (English)', validators=[DataRequired()])
    mother_name_bangla = StringField('Mother Name (বাংলা)', validators=[DataRequired()])
    mother_mobile = StringField('Mother Mobile No', validators=[
        DataRequired(), Regexp(r'^\d{10,15}$', message="Invalid mobile number")])
    mother_nid = StringField('Mother NID/Passport', validators=[DataRequired()])

    # Files
    student_photo = FileField('Student Photo', validators=[Optional()])
