import datetime
from flask import Blueprint, request

from model.employee import Employee
from services.employees_service import add_employees, get_employees
from services.stats_service import count_employees_per_department_and_job_in_2021, count_employees_per_department_greater_than_mean_in_2021

employees = Blueprint('employees',__name__)

@employees.route('/', methods= ['POST', 'GET'])
def home():
    if request.method == 'POST':
        new_employees = map(lambda employee: Employee(
            employee["name"],
            datetime.datetime.fromisoformat(employee["datetime"]),
            employee["department_id"],
            employee["job_id"]
        ), request.json)

        return str(add_employees(new_employees))
    elif request.method == 'GET':
        employees = [employee.to_dict() for employee in get_employees()]

        return employees

@employees.route("/csv", methods= ['POST'])
def csv():
    file = request.files['file']
    new_employees = [employee.replace("\r", "").split(',') for employee in file.read().decode("utf-8").split('\n')]

    new_employees = map(lambda employee: Employee(
        employee[1],
        datetime.datetime.fromisoformat(employee[2]) if employee[2] != '' else None,
        employee[3] if employee[3] != '' else None,
        employee[4] if employee[4] != '' else None,
        id = employee[0]
    ), new_employees)

    return str(add_employees(new_employees))

@employees.route('/stats/a', methods= ['GET'])
def stats_2021():
    data = count_employees_per_department_and_job_in_2021()
    data = map(lambda row: {
        "department":  row[0]
        ,"job": row[1]
        ,"Q1": row[2]
        ,"Q2": row[3]
        ,"Q3": row[4]
        ,"Q4": row[5]
    }, data)
    return list(data)

@employees.route('/stats/b', methods= ['GET'])
def stats_department():
    data = count_employees_per_department_greater_than_mean_in_2021()
    data = map(lambda row: {
        "id":  row[0]
        ,"department":  row[1]
        ,"hired": row[2]
    }, data)
    return list(data)