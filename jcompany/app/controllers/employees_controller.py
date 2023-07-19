from dateutil.parser import isoparse
from flask import Blueprint, request, Response

from app.model.employee import Employee
from app.services.employees_service import add_employees, get_employees
from app.services.stats_service import count_employees_per_department_and_job_in_2021, count_employees_per_department_greater_than_mean_in_2021

employees = Blueprint('employees',__name__)

@employees.route('/', methods= ['POST', 'GET'])
def home():
    try:
        if request.method == 'POST':
            new_employees = map(lambda employee: Employee(
                employee["name"],
                isoparse(employee["datetime"]) if employee["datetime"] != None else employee["datetime"],
                employee["department_id"],
                employee["job_id"]
            ), request.json)

            add_employees(new_employees)

            return Response(None, status=201, mimetype='application/json')
        elif request.method == 'GET':
            employees = [employee.to_dict() for employee in get_employees()]

            return employees
    except Exception as e:
        return Response(repr(e), status=400, mimetype='application/json')

@employees.route("/csv", methods= ['POST'])
def csv():
    try:
        file = request.files['file']
        new_employees = [employee.replace("\r", "").split(',') for employee in file.read().decode("utf-8").split('\n')]

        new_employees = map(lambda employee: Employee(
            employee[1],
            isoparse(employee[2]) if employee[2] != '' else None,
            employee[3] if employee[3] != '' else None,
            employee[4] if employee[4] != '' else None,
            id = employee[0]
        ), new_employees)

        add_employees(new_employees)

        return Response(None, status=201, mimetype='application/json')
    except Exception as e:
        return Response(repr(e), status=400, mimetype='application/json')