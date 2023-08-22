from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.user import User
from flask_app.models.project import Project

@app.route('/admin/dashboard')
def admin_dashboard():
    if 'id' not in session:
        return redirect('/')
    user = User.get_user_by_id({'id':session['id']})
    if user.type != 'admin':
        return redirect('/')
    
    return render_template('dashboard_admin.html', user = user)


@app.route('/accept_project/<int:project_id>',methods = ['POST'])
def accept_project(project_id):
    data_dict = {'id': project_id}
    Project.pending_to_accepted(data_dict)
    return redirect("/dashboard")

@app.route('/decline_project/<int:project_id>',methods = ['POST'])
def decline_project(project_id):
    data_dict = {'id': project_id}
    Project.decline(data_dict)
    return redirect("/dashboard")