from flask import render_template, request, redirect, session, flash
from flask_app import app

from flask_app.models.user import User

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/investors/dashboard')
def investor_dashboard():
    if 'id' not in session:
        return redirect('/')
    user = User.get_user_by_id({'id':session['id']})
    return render_template('investor_dashboard.html', user=user)


@app.route('/add_money/<int:id>', methods=['POST'])
def update_wallet(id):
    print('moneeeeyy:', request.form)
    user = User.get_user_by_id({'id':id})
    if user.wallet:
        amount = float(request.form['added_money']) + float(user.wallet) 
        data = {
            'wallet' : amount,
            'id' : id
        }
        User.update_wallet(data)
    else:
        amount = float(request.form['added_money'])
        data = {
            'wallet' : amount,
            'id' : id
        }
        User.update_wallet(data)
    return redirect('/investors/dashboard')

# @app.route('/investors/dashboard/<tab_id>')
# def redirect_to_tab(tab_id):
#     return render_template('index.html', active_tab=tab_id)


@app.route('/investors/<int:id>/update', methods = ['POST'])
def update_investor_profile(id):
    if User.validate_edit(request.form):
        print('****',request.form,'*****')
        data = {
            **request.form,
            'id':id
        }
        User.update_profile(data)
        flash('Changes Saved', "edit")
        return redirect("/investors/dashboard#profile")
    return redirect("/investors/dashboard#profile")

@app.route('/change_password', methods = ['POST'])
def update_investor_password():
    if User.change_password_validation(request.form):
        print('****',request.form,'*****')
        pw_hashed = bcrypt.generate_password_hash(request.form['new_password'])
        print(pw_hashed)
        data = {
            **request.form,
            'new_password': pw_hashed
        }
        User.update_password(data)
        flash('Password Changed!', "change_password_success")
        return redirect("/investors/dashboard#profile")
    return redirect("/investors/dashboard#profile")




