from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import User
from database import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        hashed = generate_password_hash(request.form['password'])
        user = User(username=request.form['username'], password_hash=hashed)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('login.html', mode='register')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and check_password_hash(user.password_hash, request.form['password']):
            login_user(user)
            return redirect(url_for('tasks.index'))
        flash('Invalid credentials')
    return render_template('login.html', mode='login')

@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))