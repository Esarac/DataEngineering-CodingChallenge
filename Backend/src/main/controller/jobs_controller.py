from flask import Blueprint, request

from model.job import Job
from services.jobs_service import add_jobs, get_jobs

jobs = Blueprint('jobs',__name__)

@jobs.route('/', methods= ['POST', 'GET'])
def home():
    if request.method == 'POST':
        new_jobs = map(lambda job: Job(
            job["name"]
        ), request.json)

        return str(add_jobs(new_jobs))
    elif request.method == 'GET':
        jobs = [job.to_dict() for job in get_jobs()]

        return jobs

@jobs.route("/csv", methods= ['POST'])
def csv():
    file = request.files['file']
    new_jobs = [job.replace("\r", "").split(',') for job in file.read().decode("utf-8").split('\n')] 
    new_jobs = map(lambda job: Job(
        job[1],
        id = job[0]
    ), new_jobs)

    return str(add_jobs(new_jobs))