from model.job import Job
from utils.db import db

def add_jobs(jobs: list[Job]):

    db.session.add_all(jobs)
    db.session.commit()

    return True

def get_jobs():
    return Job.query.all()