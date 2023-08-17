from flask import render_template, request, redirect, session
from flask_app import app

@app.route('/investors/dashboard')
def investor_dashboard():
    return render_template('investor_dashboard.html')