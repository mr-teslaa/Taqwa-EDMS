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
from flask import Flask,url_for,render_template,redirect,request

#   pass this app through flask
app = Flask(__name__)


#   default route of web app
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.debug=True
    app.run()
