#   importing basic module for flask
from main_app import app, db, bcrypi
from main_app.models import User
from flask import Flask
from flask import url_for
from flask import render_template
from flask import redirect
from flask import request
from flask import flash
from PIL import Image
#   importing wtf module from form.py
from main_app.form import AdmissionForm, Loginform, RegistrationForm, UpdateAccountform

#importing login from flask_login
from flask_login import login_user, current_user, logout_user, login_required


#function to save picture
def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/imgs', picture_fn)
    output_size = (125,125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn



#   default route of web app
@app.route('/')
@login_required
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

@app.route('/login', methods=['GET','POST'])
def login():
    form = Loginform()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypi.check_password_hash(user.password,form.password.data):
            print("si entre")
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            flash(f'success login {form.email.data}!','success')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:   
            flash(f'failed autentication {form.email.data}!','Danger')
    return render_template('login.html', title='Login',form=form)  

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        pass_encripted = bcrypi.generate_password_hash(form.password.data).decode('UTF-8')
        user = User(username=form.username.data,email=form.email.data,password=pass_encripted)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!','success')
        print({form.username.data})
        return redirect(url_for('login'))   
    
    return render_template('register.html', title='Register', form=form)

@app.route("/account", methods=['GET','POST'])
@login_required
def account():  
    form = UpdateAccountform()
    

    if form.validate_on_submit():
        if form.picture.data:
            print("image from form")
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file 
        
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('your account has been changed', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email    
    image = url_for('static', filename='imgs/' + current_user.image_file) 
    return render_template('account.html', title='Account', image_file=image, form=form )