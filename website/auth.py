from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

#this file is a simple authentication system for a Flask application using Flask-Login for user session management.
auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                flash("Login successful", category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash("Incorrect password", category='error')
        else:
            flash("Email not found", category='error')
    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password1')
        confirm_password = request.form.get('password2')
        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email already registered", category='error')
        if len(email) < 4:
            flash("Email must be at least 4 characters", category='error')
        elif len(username) < 2:
            flash("Username must be at least 2 characters", category='error')
        elif password != confirm_password:
            flash("Passwords don't match", category='error')
        elif len(password) < 7:
            flash("Password must be at least 7 characters", category='error')
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(password, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash("Registration successful", category='success')
            return redirect(url_for('views.home'))

    return render_template("signup.html", user=current_user)