from datetime import datetime
from math import ceil

from flask import Flask, request, render_template, redirect

from project.db.access_database import AccessDataBase

def init_app(app: Flask):
    
    @app.route('/')
    def home():
        return redirect('/reviewer/applicant/list')

    @app.route('/init')
    def initdata():
        dbobj = AccessDataBase()
        dbobj.init_data()
        return 'done'

    @app.route('/reviewer/applicant/list')
    def applicantList():
        dbobj = AccessDataBase()
        kwargs = {
            'applicants': dbobj.get_applicants(),
            'title': 'Reviewer Panel | Applicant List'
        }
        return render_template('applicant_list.jinja2', **kwargs)

    @app.route('/reviewer/applicant/details/<int:applicant_id>/', methods=['GET'])
    def applicantDetails(applicant_id):
        dbobj = AccessDataBase()
        kwargs = {
            'applicant': dbobj.get_applicant_byId(applicant_id),
            'title': 'Reviewer Panel | Applicant Details'
        }
        return render_template('applicant_view.jinja2', **kwargs)

        
        
    @app.errorhandler(404)
    def not_found(error):
        return render_template('error.jinja2', title='CRUD | NOT FOUND', warning=error), 404
    
    
    @app.errorhandler(500)
    def server_error(error):
        return render_template('error.jinja2', title='CRUD | NOT FOUND', warning=error), 500
