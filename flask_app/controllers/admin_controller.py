from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.user import User
from flask_app.models.project import Project

@app.route('/admin/dashboard')
def admin_dashboard():
    if 'id' not in session:
        return redirect('/')
    user = User.get_user_by_id({'id':session['id']})
    if user.type != 'investor':
        return redirect('/')
    
    return render_template('dashboard_admin.html', user = user)