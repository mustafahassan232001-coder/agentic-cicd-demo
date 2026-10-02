import pytest
from app import app, db
from models import User

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client

def test_registration_and_login(client):
    client.post('/register', data={'username': 'test', 'password': 'password'})
    resp = client.post('/login', data={'username': 'test', 'password': 'password'}, follow_redirects=True)
    assert b'My Tasks' in resp.data