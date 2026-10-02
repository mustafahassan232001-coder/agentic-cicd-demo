import json

def test_create_task(client):
    response = client.post('/tasks', json={'title': 'Test Task', 'description': 'Desc'})
    assert response.status_code == 201
    assert 'id' in response.get_json()

def test_get_tasks(client):
    client.post('/tasks', json={'title': 'Task 1'})
    response = client.get('/tasks')
    assert response.status_code == 200
    assert len(response.get_json()) == 1

def test_get_task_not_found(client):
    response = client.get('/tasks/999')
    assert response.status_code == 404

def test_update_task(client):
    client.post('/tasks', json={'title': 'Original'})
    response = client.put('/tasks/1', json={'title': 'Updated', 'description': 'New', 'completed': True})
    assert response.status_code == 200
    
    get_response = client.get('/tasks/1')
    data = get_response.get_json()
    assert data['title'] == 'Updated'
    assert data['completed'] == 1

def test_delete_task(client):
    client.post('/tasks', json={'title': 'To be deleted'})
    response = client.delete('/tasks/1')
    assert response.status_code == 204
    assert client.get('/tasks/1').status_code == 404
