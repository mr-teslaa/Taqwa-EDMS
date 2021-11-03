from flask import Blueprint
from flask import render_template
from flask import url_for
from flask import flash
from flask import redirect

from exam50.forms import AddMarksForm50

from main_app.models import db
from main_app.models import Marks50
from main_app.models import Marks

from flask_login import login_user
from flask_login import current_user
from flask_login import logout_user
from flask_login import login_required

exam50 = Blueprint('exam50', __name__)

# addmarks for full mark 50
@exam50.route('/50/add/marks', methods=['GET', 'POST'])
@exam50.route('/50/add/marks/', methods=['GET', 'POST'])
def addmarks50():
    form = AddMarksForm50()
    form.examname.data = '2nd'
    form.examyear.data = '2021'
    if form.validate_on_submit():
        print('I am in')
        totalmarks = Marks50(examname=form.examname.data, examyear=form.examyear.data, roll_id=form.roll_id.data, classname=form.classname.data, name=form.name.data, bengali=form.bengali.data, english=form.english.data, mathematics=form.mathematics.data, science=form.science.data, bandg=form.bandg.data, religion=form.religion.data, gpa=form.gpa.data, grade=form.grade.data, total=form.total.data)
        print('=================================')
        print(totalmarks)
        db.session.add(totalmarks)
        db.session.commit()
        flash(f'Marks successfully added for "{form.name.data}"', 'success')
        return redirect(url_for('admindashboard.dashboard'))
    print('I am out')
    print(f'Roll: {form.roll_id.data}')
    print(f'Class: {form.classname.data}')
    print(f'Name: {form.name.data}')
    print(f'Bengali: {form.bengali.data}')
    print(f'English: {form.english.data}')
    print(f'Math: {form.mathematics.data}')
    print(f'Science: {form.science.data}')
    print(f'B and G: {form.bandg.data}')
    print(f'Religion: {form.religion.data}')
    print(f'GPA: {form.gpa.data}')
    print(f'Grade: {form.grade.data}')
    print(f'Total: {form.total.data}')
    return render_template('addmarks50.html', form=form)