from flask import Blueprint
from flask import render_template
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user
from core.models import Institute
from core import db, bcrypt
from core.auth.forms import InstituteRegistrationForm, InstituteLoginForm



auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login')
def login():
    return render_template('auth/login.html')


@auth_bp.route("institute/register", methods=["GET", "POST"])
def institute_register():
    form = InstituteRegistrationForm()

    if form.validate_on_submit():
        existing_institute = Institute.query.filter_by(email=form.email.data).first()
        if existing_institute:
            flash("An institute with this email already exists.", "danger")
            return redirect(url_for("auth.institute_register"))
        institute = Institute(name=form.name.data, email=form.email.data)
        institute.set_password(form.password.data)
        db.session.add(institute)
        db.session.commit()
        flash("Your institute has been registered! You can now log in.", "success")
        return redirect(url_for("auth.institute_login"))
    print("Form validation errors:", form.errors)

    return render_template("auth/institute_register.html", form=form)



@auth_bp.route("/institute/login", methods=["GET", "POST"])
def institute_login():
    if current_user.is_authenticated:
        return redirect(url_for("institute_dashboard.institute_dashboard"))

    form = InstituteLoginForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        institute = Institute.query.filter_by(email=email).first()

        if institute and bcrypt.check_password_hash(institute.password, password):
            login_user(institute)
            next_page = request.args.get("next")
            return (
                redirect(next_page)
                if next_page
                else redirect(url_for("institute_dashboard.institute_dashboard"))
            )
        else:
            flash("Login unsuccessful. Please check email and password", "danger")

    return render_template("auth/institute_login.html", form=form)


@auth_bp.route("/institute/logout")
def institute_logout():
    logout_user()
    return redirect(url_for("auth.institute_login"))  # Ensure this matches the endpoin

