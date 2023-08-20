from flask import render_template, request, redirect, session, url_for, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.project import Project

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


# @app.route('/register/project')
# def register_project():
#     return render_template('project_registration.html')

@app.route('/project/dashboard/accepted')
def po_dashboard_accepted():
    project = Project.get_project_by_user_id({'user_id':session['id']})
    return render_template('dashboard_po_accepted.html', project = project)


@app.route('/projects/dashboard/pending')
def po_dashboard_pending():
    project = Project.get_project_by_user_id({'user_id':session['id']})
    return render_template('dashboard_po_Pending.html', project = project)



@app.route('/projects/create', methods=['POST'])
def create_project():
    print('PROJECT REQUEST FORM', request.form)
    user = User.get_user_by_id(session)
    data = {
        **request.form,
        'user_id': user.id
    }
    Project.create_project(data)
    return redirect('/projects/dashboard/pending')


@app.route('/projects/<int:project_id>/show')
def show_project(project_id):
    project = Project.get_project_by_id({'id':project_id})
    percentage = float(project.amount_raised)*100 / float(project.goal)
    user = User.get_user_by_id(session)
    return render_template("one_project_show.html", project = project ,user=user , percentage=percentage)

