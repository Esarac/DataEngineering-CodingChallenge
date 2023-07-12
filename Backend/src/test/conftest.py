import pytest
from app import create_app

@pytest.fixture()
def app():
    app = create_app("test")
    app.config.update({
        "TESTING": True,
    })

    yield client

@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def runner(app):
    return app.test_cli_runner()