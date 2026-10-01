import pytest
from app import app
from database import db
import os

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_add_task(client):
    response = client.post('/add', data={'title': 'Test Task', 'description': 'Test Desc'})
    assert response.status_code == 302
    tasks = db.get_all_tasks()
    assert any(t[1] == 'Test Task' for t in tasks)

def test_invalid_id(client):
    response = client.post('/delete/99999')
    assert response.status_code == 404

def test_empty_title_validation(client):
    response = client.post('/add', data={'title': '', 'description': 'desc'})
    assert response.status_code == 400