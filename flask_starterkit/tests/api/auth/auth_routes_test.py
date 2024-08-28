import pytest
from flask import Flask
from flask_starterkit.main.routes.auth import auth_bp

@pytest.fixture
def client():
    app = Flask(__name__)
    app.register_blueprint(auth_bp)
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_login_success(client):
    response = client.post('/login', json={'username': 'admin', 'password': 'secret'})
    assert response.status_code == 200
    assert response.get_json() == {"message": "Login successful!"}

def test_login_failure(client):
    response = client.post('/login', json={'username': 'admin', 'password': 'wrong_password'})
    assert response.status_code == 401
    assert response.get_json() == {"message": "Invalid credentials!"}
