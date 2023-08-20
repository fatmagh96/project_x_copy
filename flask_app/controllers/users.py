from flask import render_template, request, redirect, session, url_for, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.project import Project

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/dashboard')
def dashboard():
    if 'id' not in session:
        return redirect('/')
    user = User.get_user_by_id(session)
    if user.type == 'admin':
        return redirect('/admin/dashboard')
    if user.type == 'investor':
        return redirect('/investors/dashboard')
    if user.type == 'po':
        project = Project.get_project_by_user_id({'user_id':session['id']})
        if project.status == 'pending':
            return redirect('/projects/dashboard/pending')
        if project.status == 'accepted':
            return redirect('/projects/dashboard/accepted')
        

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
        if request.form['type'] == 'po':
            return redirect('/register/project')
        return redirect('/dashboard')
        
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
        return redirect('/dashboard')
    return redirect('/signin')


