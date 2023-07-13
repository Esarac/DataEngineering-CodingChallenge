import os
from dotenv import load_dotenv

from flask import Flask 

from app.utils.db import db

from app.controllers.employees_controller import employees
from app.controllers.departments_controller import departments
from app.controllers.jobs_controller import jobs
from app.controllers.stats_controller import stats

load_dotenv()
def create_app(env='prod'):
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(f"DATABASE_{env.upper()}")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.register_blueprint(employees, url_prefix='/employees')
    app.register_blueprint(departments, url_prefix='/departments')
    app.register_blueprint(jobs, url_prefix='/jobs')
    app.register_blueprint(stats, url_prefix='/stats')

    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app