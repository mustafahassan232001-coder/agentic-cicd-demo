import pytest
from app import create_app
import os

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create_and_get_tasks(client):
    res = client.post('/tasks', json={'title': 'Test Task', 'description': 'Desc'})
    assert res.status_code == 201
    res = client.get('/tasks')
    assert res.status_code == 200
    assert len(res.json) > 0

def test_get_nonexistent(client):
    res = client.get('/tasks/999')
    assert res.status_code == 404

def test_delete_task(client):
    client.post('/tasks', json={'title': 'To be deleted'})
    res = client.delete('/tasks/1')
    assert res.status_code == 204