import pytest
from fastapi.testclient import TestClient
from uuid import uuid4
from app.main import app

client = TestClient(app)

def test_add_tokens():
    response = client.post("/v1/user", json={"email": f"token_{uuid4()}@test.com", "password": "test123"})
    user_id = response.json()["id"]

    response = client.post("/v1/tokens", json={"user_id": user_id, "amount": 5})
    assert response.status_code == 200
    assert response.json()["tokens"] == 15

def test_consume_token():
    response = client.post("/v1/user", json={"email": f"consume_{uuid4()}@test.com", "password": "test123"})
    user_id = response.json()["id"]

    response = client.get(f"/v1/athlete/1?user_id={user_id}")
    assert response.status_code == 200

    response = client.get(f"/v1/user/{user_id}")
    assert response.json()["tokens"] == 9

def test_create_user():
    email = f"test_{uuid4()}@test.com"
    response = client.post("/v1/user", json={"email": email, "password": "test123"})
    assert response.status_code == 201
    assert "id" in response.json()
