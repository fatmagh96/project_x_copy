from flask import render_template, request, redirect, session
from flask_app import app
# from flask_app.models.++++ import ++++++



@app.route('/')
def index():
    return render_template('home.html')

@app.route('/registration')
def register_user():
    return render_template('registration.html')

@app.route('/explore')
def explore():
    return render_template('all_projects.html')