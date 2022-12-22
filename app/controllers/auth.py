from flask import Blueprint, render_template, request, flash
from app.models.tables import User
from app import db
import datetime
from flask_login import login_user, logout_user, login_required


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()

        if not user or not user.verify_password(password):
            flash('Please check your Log In details and try again.')
            return render_template('login.html', messageType="error")

        login_user(user)
        return render_template('projects.html', messageType="sucess")


@auth.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm-password']

        if password != confirm_password:
            flash('You need to confirm your password.')
            return render_template('register.html')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email adress already exists.')
            return render_template('register.html')

        user = User(
            name=name,
            email=email,
            password=password
        )

        db.session.add(user)
        db.session.commit()

        flash('Account registered.')
        return render_template('login.html', messageType="sucess")


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template('login.html')