from flask import Blueprint, request, jsonify, Response
import json

from app.model.department import Department
from app.services.departments_service import add_departments, get_departments

departments = Blueprint('departments',__name__)

@departments.route('/', methods= ['POST', 'GET'])
def home():
    try:
        if request.method == 'POST':
            new_departments = map(lambda department: Department(
                department["name"]
            ), request.json)

            add_departments(new_departments)

            return Response(None, status=201, mimetype='application/json')
        elif request.method == 'GET':
            departments = json.dumps([department.to_dict() for department in get_departments()])

            return Response(departments, status=200, mimetype='application/json')
    except Exception as e:
        return Response(repr(e), status=400, mimetype='application/json')

@departments.route("/csv", methods= ['POST'])
def csv():
    try:
        file = request.files['file']
        new_departments = [department.replace("\r", "").split(',') for department in file.read().decode("utf-8").split('\n')]
        new_departments = map(lambda department: Department(
            department[1],
            id = department[0]
        ), new_departments)

        add_departments(new_departments)

        return Response(None, status=201, mimetype='application/json')
    except Exception as e:
        return Response(repr(e), status=400, mimetype='application/json')