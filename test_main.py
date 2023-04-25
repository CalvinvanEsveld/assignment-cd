def test_hello_world():
    from main import main
    client = main.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b'Hello, world!'
