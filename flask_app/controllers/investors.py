from flask import render_template, request, redirect, session
from flask_app import app

from flask_app.models.user import User

@app.route('/investors/dashboard')
def investor_dashboard():
    if 'id' not in session:
        return redirect('/')
    user = User.get_user_by_id({'id':session['id']})
    return render_template('investor_dashboard.html', user=user)

@app.route('/investors/dashboard/<tab_id>')
def redirect_to_tab(tab_id):
    return render_template('index.html', active_tab=tab_id)


@app.route('/investors/<int:id>/update', methods = ['POST'])
def update_investor_profile():
    pass

