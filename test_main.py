import main

def client():
    with main.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert 'Hello, world!' in response.data
