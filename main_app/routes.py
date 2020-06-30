# import necessary file for application
from flask import render_template
from flask import url_for
from flask import redirect
from flask import request
from flask import flash

# though we use @app.route so we need to import app variable which is diclare in __init__.py
from main_app import app

# import custom form field from form.py
from main_app.form import AdmissionForm 
from main_app.form import LoginForm
from main_app.form import ApplyTeacherForm
from main_app.form import ApplyParentsForm

# import database models from models.py



#   default route of web app
@app.route('/')
def index():
    return render_template('index.html')

#   academic route for web app
@app.route('/academic')
def academic():
    return render_template('academic.html')

#   curicullam route
@app.route('/academic/curicullam')
def curicullam():
    return render_template('curicullam.html')

#   routine route
@app.route('/academic/routine')
def routine():
    return render_template('routine.html')

#   book list route
@app.route('/academic/book')
def book():
    return render_template('book.html')

#   k.g. play route
@app.route('/academic/play')
def play():
    return render_template('play.html')

#   k.g. nursary route
@app.route('/academic/nursary')
def nursary():
    return render_template('nursary.html')

#   class one route
@app.route('/academic/one')
def one():
    return render_template('one.html')

#   class two route
@app.route('/academic/two')
def two():
    return render_template('two.html')

#   class three route
@app.route('/academic/three')
def three():
    return render_template('three.html')

#   class four route
@app.route('/academic/four')
def four():
    return render_template('four.html')

#   class five routek
@app.route('/academic/five')
def five():
    return render_template('five.html')

#   class six route
@app.route('/academic/six')
def six():
    return render_template('six.html')

#   class seven route
@app.route('/academic/seven')
def seven():
    return render_template('seven.html')

#   class eight route
@app.route('/academic/eight')
def eight():
    return render_template('eight.html')

#   results route
@app.route('/results')
def results():
    return render_template('results.html')

#   notice route
@app.route('/notice')
def notice():
    return render_template('notice.html')

#   events route
@app.route('/events')
def events():
    return render_template('events.html')

#   admission route
@app.route('/admission', methods=['POST', 'GET'])
def admission():
    form = AdmissionForm()
    return render_template('admission.html', form=form)

#   apply for teacher route
@app.route('/teacher/apply', methods=['POST', 'GET'])
def applyTeacher():
    form = ApplyTeacherForm()
    return render_template('apply_teacher.html', form=form)

#   apply for parents route
@app.route('/parents/apply', methods=['POST', 'GET'])
def applyParents():
    form = ApplyParentsForm()
    return render_template('apply_parents.html', form=form)

#   login route
@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

#   login as parents route
@app.route('/parents/login', methods=['POST', 'GET'])
def loginParents():
    form = LoginForm()
    return render_template('login_parents.html', form=form)


#   about us route
@app.route('/about')
def about():
    return render_template('about.html')