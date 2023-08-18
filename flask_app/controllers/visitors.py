from flask import render_template, request, redirect, session
from flask_app import app
# from flask_app.models.++++ import ++++++



@app.route('/')
def index():
    return render_template('home.html')

@app.route('/register')
def register_user():
    #template 
    return render_template('registration.html')

@app.route('/register/project')
def register_project():
    return render_template('project_registration.html')

@app.route('/upload_project')
def upload_project():
    return render_template('project_upload.html')

@app.route('/explore')
def explore():
    return render_template('all_projects.html')

@app.route('/projects/id/show')
def project_show():
    return render_template('one_project_show.html')