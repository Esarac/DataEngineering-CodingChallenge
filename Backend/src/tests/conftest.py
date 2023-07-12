import pytest
from app import create_app, db

@pytest.fixture
def app():
    # Config
    app = create_app("test")
    app.config.update({
        "TESTING": True
        ,"WTF_CSRF_ENABLED": False
        ,"DEBUG": True
    })
    
    yield app

    # Drop Tables
    with app.app_context():
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()