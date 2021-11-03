from flask import Blueprint
from flask import render_template
from flask import url_for
from flask import flash
from flask import redirect

from main_app.exam.forms import AddMarksForm
from main_app.exam.forms import SearchExamForm

from main_app import db
from main_app.models import Marks50
from main_app.models import Marks

from flask_login import login_user
from flask_login import current_user
from flask_login import logout_user
from flask_login import login_required

exam = Blueprint('exam', __name__)

# addmarks for full marks 100
@exam.route('/add/marks', methods=['GET', 'POST'])
@exam.route('/add/marks/', methods=['GET', 'POST'])
def addmarks():
    form = AddMarksForm()
    if form.validate_on_submit():
        marks = Marks(roll_id=form.roll_id.data, classname=form.classname.data, name=form.name.data, bengali=form.bengali.data, bengali2=form.bengali2.data, english=form.english.data, english2=form.english2.data, mathematics=form.mathematics.data, science=form.science.data, bandg=form.bandg.data, religion=form.religion.data, total=form.total.data)
        db.session.add(marks)
        db.session.commit()
        flash('Marks successfully added for {form.name.data}', 'success')
        return redirect(url_for('exam.addmarks'))
    return render_template('exam/addmarks.html', form=form)


# show marks for class 6
@exam.route('/view/<string:classname>/')
@exam.route('/view/<string:classname>/')
def viewmarks(classname):
    viewmarks = Marks50.query.filter_by(classname=classname)
    viewclass = Marks50.query.filter_by(classname=classname).first()
    return render_template('viewclassresult.html', viewmarks=viewmarks, viewclass=viewclass)

# show student individual marks
@exam.route('/view/<string:classname>/<string:roll_id>/')
@exam.route('/view/<string:classname>/<string:roll_id>/')
def viewstudent(classname, roll_id):
    student = Marks50.query.filter_by(classname=classname, roll_id=roll_id).first_or_404()
    return render_template('viewstudent.html', student=student)