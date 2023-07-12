from utils.db import db

from model.department import Department
from model.job import Job

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    datetime = db.Column(db.DateTime, nullable=True)
    department_id = db.Column(db.Integer, db.ForeignKey(Department.id), nullable=True)
    job_id = db.Column(db.Integer, db.ForeignKey(Job.id), nullable=True)

    def __init__(self, name, datetime, department_id, job_id, id = None):
        self.id = id
        self.name = name
        self.datetime = datetime
        self.department_id = department_id
        self.job_id = job_id
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "datetime": self.datetime.isoformat(),
            "department_id": self.department_id,
            "job_id": self.job_id
        }
