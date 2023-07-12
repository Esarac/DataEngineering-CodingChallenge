from model.department import Department
from utils.db import db

def add_departments(departments: list[Department]):

    db.session.add_all(departments)
    db.session.commit()

    return True

def get_departments():
    return Department.query.all()