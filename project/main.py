from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash
from flask import flash, redirect, render_template, request
from markupsafe import escape
from . import create_app, db
from .user_model import User
from .routes import *

app = create_app()


def try_login(phone, password):
    # returns true if login was succesful, false if not
    
    user = User.query.filter_by(phone_number=phone).first()

    # check if the user provided correct credentials and whether user exists in the db
    if user and check_password_hash(user.password, password):
        login_user(user)
        return True

    return False

@app.route(URL_INDEX, methods=['POST', 'GET'])
def show_index_page():
    # check if user has already logged in, even if the tab has been closed, it will redirect to the home page
    if current_user.is_authenticated:
        return redirect(URL_HOME)

    if request.method == 'POST':
        if try_login(escape(request.form.get('phone_number')), escape(request.form.get('password'))):
            return redirect(URL_HOME)
        else:
            flash('Phone number or password incorrect. If you are a new user, please register first.')
            return redirect(URL_INDEX)
            
    return render_template('index.html')

@app.route(URL_LOGOUT, methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(URL_INDEX)

@app.route(URL_REGISTER, methods=['POST', 'GET'])
def show_register_form():
    if request.method == 'POST':

        # gather all the information
        name = request.form.get('name')
        surname = request.form.get('surname')
        phone_number = request.form.get('phone_number')
        password = request.form.get('password')

        # try to access the user in db
        user = User.query.filter_by(phone_number=phone_number).first()

        # check if the user already exists
        if user:
            flash('Phone number already taken')
            return redirect('register')

        new_user = User(
            phone_number = escape(phone_number), 
            name = escape(name), 
            surname = escape(surname), 
            password = escape(generate_password_hash(password, method='sha256'))
            ) 
            # ATTENTION!!!
            # sha256 is not the most secure variant, better of with the likes of bcrypt 
            # if there are plans to launch it for public audiences
        
        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)

        return redirect(URL_HOME)
        
    return render_template('register-form.html')

@app.route(URL_HOME, methods=['GET'])
@login_required
def show_users():
    users = []

    # make sure that current user is not display under: other registered users
    for user in User.query.all():
        if user.phone_number != current_user.phone_number:
            users.append(user)

    return render_template("show-users.html", users=users, user_name = current_user.name)
