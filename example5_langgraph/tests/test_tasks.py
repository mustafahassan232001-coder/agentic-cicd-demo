def test_task_isolation(client):
    # Create User A
    client.post('/register', data={'username': 'userA', 'password': 'p'}, follow_redirects=True)
    client.post('/login', data={'username': 'userA', 'password': 'p'}, follow_redirects=True)
    client.post('/add', data={'content': 'Task A'}, follow_redirects=True)
    client.get('/logout')

    # Create User B
    client.post('/register', data={'username': 'userB', 'password': 'p'}, follow_redirects=True)
    client.post('/login', data={'username': 'userB', 'password': 'p'}, follow_redirects=True)
    response = client.get('/', follow_redirects=True)
    
    assert b'Task A' not in response.data