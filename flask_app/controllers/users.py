from flask import render_template, request, redirect, session, url_for, flash
from flask_app import app
from flask_app.models.user import User

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/users/create', methods = ['POST'])
def create():
    print('USER REQUEST FORM',request.form,'****************')
    if User.validate(request.form):
        pw_hashed = bcrypt.generate_password_hash(request.form['password'])
        print(pw_hashed)
        data = {
            **request.form,
            'password': pw_hashed
        }
        user_id = User.create_user(data)
        session['id'] = user_id
        if request.form['type'] == 'investor':
            return redirect('/investors/dashboard')
        if request.form['type'] == 'po':
            return redirect('/register/project')
        
    return redirect('/register')

@app.route('/signin')
def signin():
    return render_template('login.html')

@app.route('/login', methods = ['POST'])
def login():
    # print(request.form)
    if User.login_validation(request.form):
        user = User.get_user_by_email(request.form)
        print('💲'*5,user.wallet,'💲'*5)
        session['id'] = user.id
        if user.type == 'investor':
            return redirect('/investors/dashboard')
        if user.type == 'po':
            return redirect('/project/dashboard/cyp')
        if user.type == 'admin':
            return redirect('/admin/dashboard')
    # message = "email invalid"
    return redirect('/signin')


