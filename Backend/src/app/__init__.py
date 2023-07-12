import os
from dotenv import load_dotenv

from flask import Flask 

from app.controller.employees_controller import employees
from app.controller.departments_controller import departments
from app.controller.jobs_controller import jobs

load_dotenv()
def create_app(env='prod'):
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(f"DATABASE_{env.upper()}")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.register_blueprint(employees, url_prefix='/employees')
    app.register_blueprint(departments, url_prefix='/departments')
    app.register_blueprint(jobs, url_prefix='/jobs')

    return app