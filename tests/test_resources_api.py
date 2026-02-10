from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_resource_success():
    response = client.post(
        "/resources",
        json={"name": "test-resource", "type": "demo"},
    )

    assert response.status_code == 200
    body = response.json()
    assert "id" in body
    assert body["name"] == "test-resource"
    assert body["type"] == "demo"

def test_sanity():
    assert True
