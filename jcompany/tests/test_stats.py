import json
from datetime import date
from conftest import client

from app import db
from app.model.job import Job
from app.model.department import Department
from app.model.employee import Employee

# Scenes
def scene_logic(client):
    jobs = [
        Job(name='Job 1'),
        Job(name='Job 2'),
        Job(name='Job 3')
    ]
    db.session.add_all(jobs)
    db.session.commit()

    department = [
        Department(name='Department 1'),
        Department(name='Department 2'),
        Department(name='Department 3')
    ]
    db.session.add_all(department)
    db.session.commit()

    employees = [
        #1-1
        Employee(name=f'Employee 1', datetime=date(2021, 1, 1), job_id=1, department_id=1),
        Employee(name=f'Employee 1', datetime=date(2021, 4, 1), job_id=1, department_id=1),
        Employee(name=f'Employee 1', datetime=date(2021, 12, 1), job_id=1, department_id=1),
        Employee(name=f'Employee 1', datetime=date(2021, 10, 1), job_id=1, department_id=1),
        Employee(name=f'Employee 1', datetime=date(2021, 7, 1), job_id=1, department_id=1),
        #2-1
        Employee(name=f'Employee 2', datetime=date(2021, 9, 1), job_id=2, department_id=1),
        Employee(name=f'Employee 2', datetime=date(2021, 10, 1), job_id=2, department_id=1),
        Employee(name=f'Employee 2', datetime=date(2021, 10, 1), job_id=2, department_id=1),
        Employee(name=f'Employee 2', datetime=date(2021, 12, 1), job_id=2, department_id=1),
        Employee(name=f'Employee 2', datetime=date(2021, 3, 1), job_id=2, department_id=1),
        #3-1
        Employee(name=f'Employee 3', datetime=date(2021, 6, 1), job_id=3, department_id=1),
        Employee(name=f'Employee 3', datetime=date(2021, 6, 1), job_id=3, department_id=1),
        Employee(name=f'Employee 3', datetime=date(2021, 11, 1), job_id=3, department_id=1),
        Employee(name=f'Employee 3', datetime=date(2021, 4, 1), job_id=3, department_id=1),
        #1-2
        Employee(name=f'Employee 4', datetime=date(2021, 5, 1), job_id=1, department_id=2),
        Employee(name=f'Employee 4', datetime=date(2021, 7, 1), job_id=1, department_id=2),
        Employee(name=f'Employee 4', datetime=date(2021, 4, 1), job_id=1, department_id=2),
        Employee(name=f'Employee 4', datetime=date(2021, 1, 1), job_id=1, department_id=2),
        #2-2
        Employee(name=f'Employee 5', datetime=date(2021, 3, 1), job_id=2, department_id=2),
        Employee(name=f'Employee 5', datetime=date(2021, 8, 1), job_id=2, department_id=2),
        Employee(name=f'Employee 5', datetime=date(2021, 9, 1), job_id=2, department_id=2),
        Employee(name=f'Employee 5', datetime=date(2021, 8, 1), job_id=2, department_id=2),
        #3-2
        Employee(name=f'Employee 6', datetime=date(2021, 11, 1), job_id=3, department_id=2),
        Employee(name=f'Employee 6', datetime=date(2021, 5, 1), job_id=3, department_id=2),
        Employee(name=f'Employee 6', datetime=date(2021, 8, 1), job_id=3, department_id=2),
        Employee(name=f'Employee 6', datetime=date(2021, 6, 1), job_id=3, department_id=2),
        Employee(name=f'Employee 9', datetime=date(2021, 2, 1), job_id=3, department_id=2),
        #1-3
        Employee(name=f'Employee 7', datetime=date(2021, 11, 1), job_id=1, department_id=3),
        Employee(name=f'Employee 7', datetime=date(2021, 2, 1), job_id=1, department_id=3),
        Employee(name=f'Employee 7', datetime=date(2021, 9, 1), job_id=1, department_id=3),
        #2-3
        Employee(name=f'Employee 8', datetime=date(2021, 10, 1), job_id=2, department_id=3),
        Employee(name=f'Employee 8', datetime=date(2021, 2, 1), job_id=2, department_id=3),
        Employee(name=f'Employee 8', datetime=date(2021, 7, 1), job_id=2, department_id=3),
        #3-3
        Employee(name=f'Employee 9', datetime=date(2021, 1, 1), job_id=3, department_id=3),
        Employee(name=f'Employee 9', datetime=date(2021, 3, 1), job_id=3, department_id=3),
        Employee(name=f'Employee 9', datetime=date(2021, 5, 1), job_id=3, department_id=3)
    ]
    db.session.add_all(employees)
    db.session.commit()

def scene_structure(client):
    jobs = [
        Job(name='Job'),
        Job(name='Job'),
        Job(name='Job'),
        Job(name='Job'),
    ]
    db.session.add_all(jobs)
    db.session.commit()

    department = [
        Department(name='Department'),
        Department(name='Department'),
        Department(name='Department')
    ]
    db.session.add_all(department)
    db.session.commit()

    employees = [
        Employee(name=f'Employee', datetime=date(2021, 1, 1), job_id=1, department_id=1),
        Employee(name=f'Employee', datetime=date(2021, 1, 1), job_id=1, department_id=2),
        Employee(name=f'Employee', datetime=date(2021, 1, 1), job_id=1, department_id=3),
        Employee(name=f'Employee', datetime=date(2021, 1, 1), job_id=2, department_id=1),
        Employee(name=f'Employee', datetime=date(2021, 1, 1), job_id=2, department_id=2),
        Employee(name=f'Employee', datetime=date(2021, 1, 1), job_id=3, department_id=1),
        Employee(name=f'Employee', datetime=date(2021, 1, 1), job_id=3, department_id=2),
        Employee(name=f'Employee', datetime=date(2021, 1, 1), job_id=4, department_id=1),
        Employee(name=f'Employee', datetime=date(2021, 1, 1), job_id=4, department_id=2),
    ]
    db.session.add_all(employees)
    db.session.commit()

class TestA:
    def test_a_logic(self, client):
        scene_logic(client)

        response = client.get('/stats/a')

        assert response.status_code == 200

        response_data = json.loads(response.data)

        assert len(response_data) == 9
        #3-3
        assert response_data[0]['Q1'] == 2
        assert response_data[0]['Q2'] == 1
        assert response_data[0]['Q3'] == 0
        assert response_data[0]['Q4'] == 0
        #2-3
        assert response_data[1]['Q1'] == 1
        assert response_data[1]['Q2'] == 0
        assert response_data[1]['Q3'] == 1
        assert response_data[1]['Q4'] == 1
        #1-3
        assert response_data[2]['Q1'] == 1
        assert response_data[2]['Q2'] == 0
        assert response_data[2]['Q3'] == 1
        assert response_data[2]['Q4'] == 1
        #3-2
        assert response_data[3]['Q1'] == 1
        assert response_data[3]['Q2'] == 2
        assert response_data[3]['Q3'] == 1
        assert response_data[3]['Q4'] == 1
        #2-2
        assert response_data[4]['Q1'] == 1
        assert response_data[4]['Q2'] == 0
        assert response_data[4]['Q3'] == 3
        assert response_data[4]['Q4'] == 0
        #1-2
        assert response_data[5]['Q1'] == 1
        assert response_data[5]['Q2'] == 2
        assert response_data[5]['Q3'] == 1
        assert response_data[5]['Q4'] == 0
        #3-1
        assert response_data[6]['Q1'] == 0
        assert response_data[6]['Q2'] == 3
        assert response_data[6]['Q3'] == 0
        assert response_data[6]['Q4'] == 1
        #2-1
        assert response_data[7]['Q1'] == 1
        assert response_data[7]['Q2'] == 0
        assert response_data[7]['Q3'] == 1
        assert response_data[7]['Q4'] == 3
        #1-1
        assert response_data[8]['Q1'] == 1
        assert response_data[8]['Q2'] == 1
        assert response_data[8]['Q3'] == 1
        assert response_data[8]['Q4'] == 2
    
    def test_a_structure(self, client):
        scene_structure(client)

        response = client.get('/stats/a')

        assert response.status_code == 200

        response_data = json.loads(response.data)

        assert len(response_data) == 9
    
    def test_a_empty(self, client):
        response = client.get('/stats/a')

        assert response.status_code == 200

        response_data = json.loads(response.data)

        assert len(response_data) == 0

class TestB:
    def test_b_logic(self, client):
        scene_logic(client)

        response = client.get('/stats/b')

        assert response.status_code == 200

        response_data = json.loads(response.data)
        print(response_data)

        assert len(response_data) == 2
        # Department 1
        assert response_data[0]['hired'] == 14
        assert response_data[1]['hired'] == 13
    
    def test_b_structure(self, client):
        scene_structure(client)

        response = client.get('/stats/b')

        assert response.status_code == 200

        response_data = json.loads(response.data)

        assert len(response_data) == 2
    
    def test_b_empty(self, client):
        response = client.get('/stats/b')

        assert response.status_code == 200

        response_data = json.loads(response.data)

        assert len(response_data) == 0