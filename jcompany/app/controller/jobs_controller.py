from flask import Blueprint, request, Response

from app.model.job import Job
from app.services.jobs_service import add_jobs, get_jobs

jobs = Blueprint('jobs',__name__)

@jobs.route('/', methods= ['POST', 'GET'])
def home():
    try:
        if request.method == 'POST':
            new_jobs = map(lambda job: Job(
                job["name"]
            ), request.json)

            add_jobs(new_jobs)

            return Response(None, status=201, mimetype='application/json')
        elif request.method == 'GET':
            jobs = [job.to_dict() for job in get_jobs()]

            return jobs
    except Exception as e:
        return Response(repr(e), status=400, mimetype='application/json')

@jobs.route("/csv", methods= ['POST'])
def csv():
    try:
        file = request.files['file']
        new_jobs = [job.replace("\r", "").split(',') for job in file.read().decode("utf-8").split('\n')] 
        new_jobs = map(lambda job: Job(
            job[1],
            id = job[0]
        ), new_jobs)

        add_jobs(new_jobs)

        return Response(None, status=201, mimetype='application/json')
    except Exception as e:
        return Response(repr(e), status=400, mimetype='application/json')