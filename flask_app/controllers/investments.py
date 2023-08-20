from flask import render_template, request, redirect, session, flash, url_for
from flask_app import app

from flask_app.models.user import User
from flask_app.models.project import Project
from flask_app.models.investment import Investment


@app.route('/investments/new/<int:project_id>', methods=['POST'])
def make_investments(project_id):
    user = User.get_user_by_id({'id':request.form['user_id']})
    if request.form['amount'] <= user.wallet:
        data = {
            **request.form,
            'project_id':project_id
        }
        Investment.make_investment(data)
        amount =  float(user.wallet) - float(request.form['amount'])
        data_wallet = {
            'wallet' : amount,
            'id' : id
        }
        User.update_wallet(data_wallet)
        flash("Successful Transaction!" , "investment_success")
        return redirect(f"/projects/{project_id}/show")
    flash("Insufficient funds in Wallet", "investment_danger")
    return redirect(f"/projects/{project_id}/show")