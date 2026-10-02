import pytest
from app import app
from database import init_db
import os

@pytest.fixture
def client():
    app.config['TESTING'] = True
    init_db()
    with app.test_client() as client:
        yield client

def test_create_task(client):
    rv = client.post('/tasks', json={'title': 'Test Task', 'description': 'Desc'})
    assert rv.status_code == 201

def test_get_tasks(client):
    rv = client.get('/tasks')
    assert rv.status_code == 200
    assert isinstance(rv.json, list)

def test_get_task_404(client):
    rv = client.get('/tasks/999')
    assert rv.status_code == 404

def test_delete_task(client):
    client.post('/tasks', json={'title': 'To be deleted'})
    rv = client.delete('/tasks/1')
    assert rv.status_code == 204
