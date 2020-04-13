# ========================================================================== #
#                           Junior School and College
#                    A School Management System with FLASK
#   
#       Create by some intelligent programmer
#       Full CRUD facility
#   
#       Github: https://github.com/hacker-tesla/Junior_School_and_College
# ========================================================================== #










#   importing basic module for flask
from flask import Flask
from flask import url_for
from flask import render_template
from flask import redirect
from flask import request

#   importing wtf module from form.py
from form import AdmissionForm

#   pass this app through flask
app = Flask(__name__)



#   genarate a secret key
app.config['SECRET_KEY'] = '248fb9a5bdffa13c0bc136504ebf75c2'



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


#   about us route
@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.debug=True
    app.run()