import pytest
from app import app as flask_app

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_hello(client):
    res = client.get("/hello")
    assert res.status_code == 200
    assert res.json == {"msg": "HELLO WORLD"}

def test_add(client):
    res = client.post("/add", json={"number1" : 1, "number2" : 2})
    assert res.status_code == 200
    assert res.json == {"result": 3}

    res = client.post("/add", json={"number1" : 1, "number2" : "a"})
    assert res.status_code == 400
    assert res.json == {"error": "Invalid input"}
    