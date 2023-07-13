import io
from werkzeug.datastructures import FileStorage

import json
from datetime import date
from conftest import client

from app import db
from app.model.job import Job
from app.model.department import Department
from app.model.employee import Employee

# Scenes
def scene_jobs_and_departments(client):
	with client.application.app_context():
		jobs = [
			Job(name=f'Job {i}') for i in range(1, 183+1)
		]
		db.session.add_all(jobs)
		db.session.commit()

		department = [
			Department(name=f'Department {i}') for i in range(1, 12+1)
		]
		db.session.add_all(department)
		db.session.commit()

def scene_default(client):
	scene_jobs_and_departments(client)

	with client.application.app_context():
		db.session.add(Employee(name='Employee 1', datetime=date.fromisoformat('2023-07-12'), job_id=1, department_id=1))
		db.session.add(Employee(name='Employee 2', datetime=date.fromisoformat('2023-07-12'), job_id=1, department_id=2))
		db.session.add(Employee(name='Employee 3', datetime=date.fromisoformat('2023-07-12'), job_id=2, department_id=1))
		db.session.add(Employee(name='Employee 4', datetime=date.fromisoformat('2023-07-12'), job_id=2, department_id=2))

		db.session.commit()

class TestGet:
	def test_jobs_get(self, client):
		scene_default(client)

		url = '/employees/'

		response = client.get(url)

		assert response.status_code == 200

		response_data = json.loads(response.data)

		assert len(response_data) == 4
		assert response_data[0]['name'] == 'Employee 1'
		assert response_data[0]['datetime'] == '2023-07-12T00:00:00'
		assert response_data[0]['job_id'] == 1
		assert response_data[0]['department_id'] == 1
		assert response_data[1]['name'] == 'Employee 2'
		assert response_data[1]['datetime'] == '2023-07-12T00:00:00'
		assert response_data[1]['job_id'] == 1
		assert response_data[1]['department_id'] == 2
		assert response_data[2]['name'] == 'Employee 3'
		assert response_data[2]['datetime'] == '2023-07-12T00:00:00'
		assert response_data[2]['job_id'] == 2
		assert response_data[2]['department_id'] == 1
		assert response_data[3]['name'] == 'Employee 4'
		assert response_data[3]['datetime'] == '2023-07-12T00:00:00'
		assert response_data[3]['job_id'] == 2
		assert response_data[3]['department_id'] == 2

class TestPost:
	def test_employees_post_normal(self, client):
		scene_jobs_and_departments(client)

		mimetype = 'application/json'
		headers = {
			'Content-Type': mimetype,
			'Accept': mimetype
		}
		data = [
			{
				'name': 'Employee 1',
				'datetime': '2023-07-12',
				'job_id': 1,
				'department_id': 1
			},
			{
				'name': 'Employee 2',
				'datetime': None,
				'job_id': 1,
				'department_id': 2
			},
			{
				'name': 'Employee 3',
				'datetime': '2023-07-12',
				'job_id': None,
				'department_id': 1
			},
			{
				'name': 'Employee 4',
				'datetime': '2023-07-12',
				'job_id': 2,
				'department_id': None
			}
		]
		url = '/employees/'

		response = client.post(url, headers=headers, data=json.dumps(data))

		assert response.status_code == 201
		assert response.data.decode('utf-8') == ''

		with client.application.app_context():
			assert db.session.query(Employee).count() == 4
			assert db.session.query(Employee).filter(Employee.name == 'Employee 1').count() == 1
			assert db.session.query(Employee).filter(Employee.name == 'Employee 2').count() == 1
			assert db.session.query(Employee).filter(Employee.name == 'Employee 3').count() == 1
			assert db.session.query(Employee).filter(Employee.name == 'Employee 4').count() == 1

	def test_employees_post_empty(self, client):
		mimetype = 'application/json'
		headers = {
			'Content-Type': mimetype,
			'Accept': mimetype
		}
		data = []
		url = '/employees/'

		response = client.post(url, headers=headers, data=json.dumps(data))

		assert response.status_code == 201
		assert response.data.decode('utf-8') == ''

		with client.application.app_context():
			assert db.session.query(Employee).count() == 0
	
	def test_employees_post_invalid(self, client):
		scene_jobs_and_departments(client)

		mimetype = 'application/json'
		headers = {
			'Content-Type': mimetype,
			'Accept': mimetype
		}
		data = [
			{
				'name': 'Employee 1',
				'datetime': '2023-07-12',
				'job_id': 1,
				'department_id': 1
			},
			{
				'name': 'Employee 2',
				'datetime': '2023-07-12',
				'job_id': 1,
				'lastname':"lastname",
				'department_id': 2
			},
			{
				'name': 'Employee 3',
				'job_id': 2,
				'department_id': 1
			},
			{
				'name': 'Employee 4',
				'datetime': '2023-07-12',
				'job_id': 2,
				'department_id': 2
			}
		]
		url = '/employees/'

		response = client.post(url, headers=headers, data=json.dumps(data))

		assert response.status_code == 400
		assert response.data.decode('utf-8') == "KeyError('datetime')"

		with client.application.app_context():
			assert db.session.query(Employee).count() == 0
	
	def test_employees_post_invalid_datetime(self, client):
		scene_jobs_and_departments(client)

		mimetype = 'application/json'
		headers = {
			'Content-Type': mimetype,
			'Accept': mimetype
		}
		data = [
			{
				'name': 'Employee 1',
				'datetime': '2023-07-12',
				'job_id': 1,
				'department_id': 1
			},
			{
				'name': 'Employee 2',
				'datetime': '2023-07-12',
				'job_id': 1,
				'department_id': 2
			},
			{
				'name': 'Employee 3',
				'datetime': 'Hello World',
				'job_id': 2,
				'department_id': 1
			},
			{
				'name': 'Employee 4',
				'datetime': '2023-07-12',
				'job_id': 2,
				'department_id': 2
			}
		]
		url = '/employees/'

		response = client.post(url, headers=headers, data=json.dumps(data))

		print(response.data.decode('utf-8'))
		assert response.status_code == 400
		assert response.data.decode('utf-8') == "ValueError(\"Invalid isoformat string: 'Hello World'\")"

		with client.application.app_context():
			assert db.session.query(Employee).count() == 0
	
	def test_employees_post_invalid_job(self, client):
		scene_jobs_and_departments(client)

		mimetype = 'application/json'
		headers = {
			'Content-Type': mimetype,
			'Accept': mimetype
		}
		data = [
			{
				'name': 'Employee 1',
				'datetime': '2023-07-12',
				'job_id': 1,
				'department_id': 1
			},
			{
				'name': 'Employee 2',
				'datetime': None,
				'job_id': 1,
				'department_id': 2
			},
			{
				'name': 'Employee 3',
				'datetime': '2023-07-12',
				'job_id': 0,
				'department_id': 1
			},
			{
				'name': 'Employee 4',
				'datetime': '2023-07-12',
				'job_id': 2,
				'department_id': None
			}
		]
		url = '/employees/'

		response = client.post(url, headers=headers, data=json.dumps(data))

		assert response.status_code == 400
		assert 'foreign key constraint fails' in response.data.decode('utf-8')

		with client.application.app_context():
			assert db.session.query(Employee).count() == 0
	
	def test_employees_post_invalid_department(self, client):
		scene_jobs_and_departments(client)

		mimetype = 'application/json'
		headers = {
			'Content-Type': mimetype,
			'Accept': mimetype
		}
		data = [
			{
				'name': 'Employee 1',
				'datetime': '2023-07-12',
				'job_id': 1,
				'department_id': 1
			},
			{
				'name': 'Employee 2',
				'datetime': None,
				'job_id': 1,
				'department_id': 2
			},
			{
				'name': 'Employee 3',
				'datetime': '2023-07-12',
				'job_id': 2,
				'department_id': 0
			},
			{
				'name': 'Employee 4',
				'datetime': '2023-07-12',
				'job_id': 2,
				'department_id': None
			}
		]
		url = '/employees/'

		response = client.post(url, headers=headers, data=json.dumps(data))

		assert response.status_code == 400
		assert 'foreign key constraint fails' in response.data.decode('utf-8')

		with client.application.app_context():
			assert db.session.query(Employee).count() == 0
	
	def test_employees_post_1000(self, client):
		scene_jobs_and_departments(client)

		mimetype = 'application/json'
		headers = {
			'Content-Type': mimetype,
			'Accept': mimetype
		}
		data = [
			{
				'name': f'Employee {i}',
				'datetime': '2023-07-12',
				'job_id': 1,
				'department_id': 1
			} for i in range(1000)
		]
		url = '/employees/'

		response = client.post(url, headers=headers, data=json.dumps(data))

		assert response.status_code == 201
		assert response.data.decode('utf-8') == ''

		with client.application.app_context():
			assert db.session.query(Employee).count() == 1000

class TestCSV:
	CSV_GOOD_PATH = 'tests/scenes/employees.csv'
	CSV_BAD_PATH_1 = 'tests/scenes/employees_invalid.csv'
	CSV_BAD_PATH_2 = 'tests/scenes/employees_invalid_date.csv'

	def test_employees_csv_normal(self, client):
		scene_jobs_and_departments(client)

		mimetype = 'multipart/form-data'
		headers = {
			'Content-Type': mimetype,
			'Accept': mimetype
		}
		url = '/employees/csv'

		# Read the CSV file
		with open(self.CSV_GOOD_PATH, 'rb') as file:
			csv_data = file.read()
		csv_file = FileStorage(
			stream=io.BytesIO(csv_data),
			filename='csv_file.csv',
			content_type='text/csv'
		)
		files = {'file': (csv_file, 'csv_file.csv')}

		response = client.post(url, data=files, headers=headers)

		assert response.status_code == 201
		assert response.data.decode("utf-8") == ''

		with client.application.app_context():
			assert db.session.query(Employee).count() == 1999
	
	def test_employees_csv_invalid_id(self, client):
		scene_jobs_and_departments(client)

		mimetype = 'multipart/form-data'
		headers = {
			'Content-Type': mimetype,
			'Accept': mimetype
		}
		url = '/employees/csv'

		# Read the CSV file
		with open(self.CSV_BAD_PATH_1, 'rb') as file:
			csv_data = file.read()
		csv_file = FileStorage(
			stream=io.BytesIO(csv_data),
			filename='csv_file.csv',
			content_type='text/csv'
		)
		files = {'file': (csv_file, 'csv_file.csv')}

		response = client.post(url, data=files, headers=headers)

		assert response.status_code == 400
		assert "Incorrect integer value: \\'\\' for column \\'id\\'" in response.data.decode("utf-8")

		with client.application.app_context():
			assert db.session.query(Employee).count() == 0
	
	def test_employees_csv_invalid_datetime(self, client):
		scene_jobs_and_departments(client)

		mimetype = 'multipart/form-data'
		headers = {
			'Content-Type': mimetype,
			'Accept': mimetype
		}
		url = '/employees/csv'

		# Read the CSV file
		with open(self.CSV_BAD_PATH_2, 'rb') as file:
			csv_data = file.read()
		csv_file = FileStorage(
			stream=io.BytesIO(csv_data),
			filename='csv_file.csv',
			content_type='text/csv'
		)
		files = {'file': (csv_file, 'csv_file.csv')}

		response = client.post(url, data=files, headers=headers)

		assert response.status_code == 400
		assert "Invalid isoformat string" in response.data.decode("utf-8")

		with client.application.app_context():
			assert db.session.query(Employee).count() == 0

	def test_employees_csv_already(self, client):
		scene_default(client)

		mimetype = 'multipart/form-data'
		headers = {
			'Content-Type': mimetype,
			'Accept': mimetype
		}
		url = '/employees/csv'

		# Read the CSV file
		with open(self.CSV_GOOD_PATH, 'rb') as file:
			csv_data = file.read()
		csv_file = FileStorage(
			stream=io.BytesIO(csv_data),
			filename='csv_file.csv',
			content_type='text/csv'
		)
		files = {'file': (csv_file, 'csv_file.csv')}

		response = client.post(url, data=files, headers=headers)

		assert response.status_code == 400
		assert "Duplicate entry" in response.data.decode("utf-8")

		with client.application.app_context():
			assert db.session.query(Employee).count() == 4
	
	def test_employees_csv_json(self, client):
		scene_jobs_and_departments(client)

		mimetype = 'application/json'
		headers = {
			'Content-Type': mimetype,
			'Accept': mimetype
		}
		data = [
			{
				'name': 'Employee 1',
				'datetime': '2023-07-12',
				'job_id': 1,
				'department_id': 1
			}
		]
		url = '/employees/csv'

		response = client.post(url, data=json.dumps(data), headers=headers)

		assert response.status_code == 400
		assert 'Bad Request' in response.data.decode("utf-8")

		with client.application.app_context():
			assert db.session.query(Employee).count() == 0
