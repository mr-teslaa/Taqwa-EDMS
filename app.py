# ========================================================================== #
#                           Junior School and College
#                    A School Management System with FLASK
#   
#       Create by some intelligent programmer
#       Full CRUD facility
#   
#       Github: https://github.com/hacker-tesla/Junior_School_and_College
# ========================================================================== #










#   importin basic module for flask
from flask import Flask
from flask import url_for
from flask import render_template
from flask import redirect
from flask import request

#   pass this app through flask
app = Flask(__name__)


#   default route of web app
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.debug=True
    app.run()