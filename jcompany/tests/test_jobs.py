import io
from werkzeug.datastructures import FileStorage

import json
from conftest import client
from app import db
from app.model.job import Job

# Scenes
def scene_default(client):
	with client.application.app_context():
		db.session.add(Job(name='Job 1'))
		db.session.add(Job(name='Job 2'))
		db.session.add(Job(name='Job 3'))
		db.session.commit()

# Tests
class TestGet:
	def test_jobs_get(self, client):
		scene_default(client)

		url = '/jobs/'

		response = client.get(url)

		assert response.status_code == 200

		response_data = json.loads(response.data)

		assert len(response_data) == 3
		assert response_data[0]['name'] == 'Job 1'
		assert response_data[1]['name'] == 'Job 2'
		assert response_data[2]['name'] == 'Job 3'

class TestPost:
	def test_jobs_post_normal(self, client):
		mimetype = 'application/json'
		headers = {
			'Content-Type': mimetype,
			'Accept': mimetype
		}
		data = [
			{
				'name': 'Job 1'
			},
			{
				'name': 'Job 2'
			},
			{
				'name': 'Job 3'
			}
		]
		url = '/jobs/'

		response = client.post(url, data=json.dumps(data), headers=headers)

		assert response.status_code == 201
		assert response.data.decode("utf-8") == ''

		with client.application.app_context():
			assert db.session.query(Job).count() == 3
			assert db.session.query(Job).filter(Job.name == 'Job 1').count() == 1
			assert db.session.query(Job).filter(Job.name == 'Job 2').count() == 1
			assert db.session.query(Job).filter(Job.name == 'Job 3').count() == 1
    
	def test_jobs_post_empty(self, client):
		mimetype = 'application/json'
		headers = {
			'Content-Type': mimetype,
			'Accept': mimetype
		}
		data = []
		url = '/jobs/'

		response = client.post(url, data=json.dumps(data), headers=headers)

		assert response.status_code == 201
		assert response.data.decode("utf-8") == ''

		with client.application.app_context():
			assert db.session.query(Job).count() == 0
	
	def test_jobs_post_invalid(self, client):
		mimetype = 'application/json'
		headers = {
			'Content-Type': mimetype,
			'Accept': mimetype
		}
		data = [
			{
				'name': 'Job 1'
			},
			{
				'lastname': 'Job 2'
			},
			{
				'name': 'Job 3'
			}
		]
		url = '/jobs/'

		response = client.post(url, data=json.dumps(data), headers=headers)

		assert response.status_code == 400

		assert response.data.decode("utf-8") == "KeyError('name')"

		with client.application.app_context():
			assert db.session.query(Job).count() == 0
		
	def test_jobs_post_1000(self, client):
		mimetype = 'application/json'
		headers = {
			'Content-Type': mimetype,
			'Accept': mimetype
		}
		data = [
			{
				'name': 'Job ' + str(i)
			} for i in range(1000)
		]
		url = '/jobs/'

		response = client.post(url, data=json.dumps(data), headers=headers)

		assert response.status_code == 201
		assert response.data.decode("utf-8") == ''

		with client.application.app_context():
			assert db.session.query(Job).count() == 1000

class TestCSV:
	CSV_GOOD_PATH = 'tests/scenes/jobs.csv'
	CSV_BAD_PATH = 'tests/scenes/jobs_invalid.csv'

	def test_jobs_csv_normal(self, client):
		mimetype = 'multipart/form-data'
		headers = {
			'Content-Type': mimetype,
			'Accept': mimetype
		}
		url = '/jobs/csv'

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
			assert db.session.query(Job).count() == 183
	
	def test_jobs_csv_invalid(self, client):
		mimetype = 'multipart/form-data'
		headers = {
			'Content-Type': mimetype,
			'Accept': mimetype
		}
		url = '/jobs/csv'

		# Read the CSV file
		with open(self.CSV_BAD_PATH, 'rb') as file:
			csv_data = file.read()
		csv_file = FileStorage(
			stream=io.BytesIO(csv_data),
			filename='csv_file.csv',
			content_type='text/csv'
		)
		files = {'file': (csv_file, 'csv_file.csv')}

		response = client.post(url, data=files, headers=headers)

		assert response.status_code == 400
		assert "for column \\\'id\\\' at row 7"  in response.data.decode("utf-8")

		with client.application.app_context():
			assert db.session.query(Job).count() == 0
	
	def test_jobs_csv_already(self, client):
		scene_default(client)

		mimetype = 'multipart/form-data'
		headers = {
			'Content-Type': mimetype,
			'Accept': mimetype
		}
		url = '/jobs/csv'

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
		assert 'Duplicate entry' in response.data.decode("utf-8")

		with client.application.app_context():
			assert db.session.query(Job).count() == 3
	
	def test_jobs_csv_json(self, client):
		mimetype = 'application/json'
		headers = {
			'Content-Type': mimetype,
			'Accept': mimetype
		}
		data = [
			{
				'name': 'Job 1'
			}
		]
		url = '/jobs/csv'

		response = client.post(url, data=json.dumps(data), headers=headers)

		assert response.status_code == 400
		assert 'Bad Request' in response.data.decode("utf-8")

		with client.application.app_context():
			assert db.session.query(Job).count() == 0