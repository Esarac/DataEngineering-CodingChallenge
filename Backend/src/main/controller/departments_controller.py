from flask import Blueprint, request, jsonify

from model.department import Department
from services.departments_service import add_departments, get_departments

departments = Blueprint('departments',__name__)

@departments.route('/', methods= ['POST', 'GET'])
def home():
    if request.method == 'POST':
        new_departments = map(lambda department: Department(
            department["name"]
        ), request.json)

        return str(add_departments(new_departments))
    elif request.method == 'GET':
        departments = [department.to_dict() for department in get_departments()]

        return departments

@departments.route("/csv", methods= ['POST'])
def csv():
    file = request.files['file']
    new_departments = [department.replace("\r", "").split(',') for department in file.read().decode("utf-8").split('\n')]
    new_departments = map(lambda department: Department(
        department[1],
        id = department[0]
    ), new_departments)
    return str(add_departments(new_departments))