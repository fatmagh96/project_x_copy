from flask import render_template, request, redirect, session
from flask_app import app

@app.route('/admin/dashboard')
def admin_dashboard():
    return render_template('dashboard_admin.html')