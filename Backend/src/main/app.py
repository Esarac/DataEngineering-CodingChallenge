import os
import unittest
from dotenv import load_dotenv

from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

from controller.employees_controller import employees
from controller.departments_controller import departments
from controller.jobs_controller import jobs

load_dotenv()
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:admin@localhost:3306/jcompany' #os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(employees, url_prefix='/employees')
app.register_blueprint(departments, url_prefix='/departments')
app.register_blueprint(jobs, url_prefix='/jobs')