from test.conftest import client

def test_should_status_code_ok(client):
	response = client.get('/departments')
	assert response.status_code == 200