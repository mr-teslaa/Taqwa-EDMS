 # import necessary file for application
from flask import render_template, current_app as app

#   default route of web app
@app.route('/')
# @app.route('/dashboard')
def index():
    return render_template('index.html')

# Dashboard route
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

#   about us route
@app.route('/about')
def about():
    return render_template('about.html')
