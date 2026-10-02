import pytest
from app import app, db
from models import Task, User
from flask_login import login_user

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client

def test_task_authorization(client):
    # Ensure user cannot access tasks without login
    resp = client.get('/', follow_redirects=True)
    assert b'Login' in resp.data