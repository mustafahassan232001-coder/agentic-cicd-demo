def test_registration_and_login(client):
    # Test Registration
    response = client.post('/register', data={'username': 'testuser', 'password': 'password123'}, follow_redirects=True)
    assert response.status_code == 200
    
    # Test Login
    response = client.post('/login', data={'username': 'testuser', 'password': 'password123'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Tasks' in response.data

def test_invalid_login(client):
    response = client.post('/login', data={'username': 'unknown', 'password': 'wrongpassword'}, follow_redirects=True)
    assert b'Invalid username or password' in response.data