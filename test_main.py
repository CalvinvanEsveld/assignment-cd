import main

@pytest.fixture
def test_client():
    flask_app = create_app()
    testing_client = flask_app.test_client()
 
    ctx = flask_app.app_context()
    ctx.push()
 
    yield testing_client  # this line is the actual test client object
 
    ctx.pop()


def test_hello_world():
    client = main.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b'Hello, world!'
