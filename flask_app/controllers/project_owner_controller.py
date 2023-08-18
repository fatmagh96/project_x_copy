from flask import render_template, request, redirect, session
from flask_app import app

@app.route('/project/dashboard/accepted')
def po_dashboard_accepted():
    return render_template('dashboard_po_accepted.html')

@app.route('/project/dashboard/cyp')
def po_dashboard_cyp():
    return render_template('dashboard_po_CYP.html')

@app.route('/project/dashboard/pending')
def po_dashboard_pending():
    return render_template('dashboard_po_Pending.html')

