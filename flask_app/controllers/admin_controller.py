from flask import render_template, request, redirect, session, send_file
from flask_app import app
from flask_app.models.user import User
from flask_app.models.project import Project

import os

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

@app.route('/download/<path:document_name>')
def download_document(document_name):
    # Validate the document_name and construct the file path
    document_path = os.path.join('c:/Users/fghra/OneDrive/Bureau/Coding_Dojo/project_copy/project_x_copy/flask_app', document_name)

    # Check if the file exists
    if os.path.exists(document_path):
        return send_file(document_path, as_attachment=True)
    else:
        return "Document not found", 404





# @app.route('/download/<filename>', methods=['GET'])
# def download_file(filename):
#     file_path = 'uploads/' + filename
#     return send_file(file_path, as_attachment=True)