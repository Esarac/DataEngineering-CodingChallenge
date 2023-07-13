import datetime
from flask import Blueprint, request, Response

from app.services.stats_service import count_employees_per_department_and_job_in_2021, count_employees_per_department_greater_than_mean_in_2021

stats = Blueprint('stats',__name__)

@stats.route('/a', methods= ['GET'])
def stats_2021():
    data = count_employees_per_department_and_job_in_2021()
    data = map(lambda row: {
        "department":  row[0]
        ,"job": row[1]
        ,"Q1": int(row[2])
        ,"Q2": int(row[3])
        ,"Q3": int(row[4])
        ,"Q4": int(row[5])
    }, data)
    return list(data)

@stats.route('/b', methods= ['GET'])
def stats_department():
    data = count_employees_per_department_greater_than_mean_in_2021()
    data = map(lambda row: {
        "id":  row[0]
        ,"department":  row[1]
        ,"hired": row[2]
    }, data)
    return list(data)