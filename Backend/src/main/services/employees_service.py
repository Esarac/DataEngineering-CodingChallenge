from model.employee import Employee
from utils.db import db

def add_employees(employees: list[Employee]):

    db.session.add_all(employees)
    db.session.commit()

    return True

def get_employees():
    return Employee.query.all()