from flask import Blueprint, render_template, redirect, url_for, flash
from travel.forms import LoginForm, RegistrationForm
from .models import User
from . import db
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user

authbp = Blueprint('auth', __name__)

@authbp.route('/login', methods = ['GET', 'POST'])
def login():
    loginForm = LoginForm()
    error = None
    if loginForm.validate_on_submit():
        username = loginForm.username.data
        password = loginForm.password.data
        user = db.session.scalar(db.select(User).where(User.name==username))

        if user is None or not check_password_hash(user.password_hash, password):
            error = 'Incorrect username or password'
        
        if error is None:
            login_user(user)
            return redirect(url_for('main.index'))
        else:
            flash(error)
    return render_template('user.html', form=loginForm, heading='login')

@authbp.route('/register', methods = ['GET', 'POST'])
def register():
    registerForm = RegistrationForm()
    if registerForm.validate_on_submit():
        username = registerForm.username.data
        password = registerForm.password.data
        email = registerForm.email.data

        user = db.session.scalar(db.select(User).where(User.name == username))
        if user:
            flash('Username already exists, try another')
            return (redirect(url_for('auth.register')))
        
        password_hash = generate_password_hash(password)
        new_user = User(name = username, password_hash = password_hash, emailid = email)
        db.session.add(new_user)
        db.session.commit()

        flash('Registered Successfully')
        return redirect(url_for('main.index'))
    
    else: 
        return render_template('user.html', form=registerForm, heading='Register')

@authbp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))