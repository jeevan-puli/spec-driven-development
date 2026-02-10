from fastapi.testclient import TestClient

from app.main import app, resources

client = TestClient(app)


def setup_function():
    # Ensure deterministic tests by clearing in-memory storage
    resources.clear()


def test_create_resource_success():
    response = client.post(
        "/resources",
        json={"name": "resource-1", "type": "demo"},
    )

    assert response.status_code == 200
    body = response.json()

    assert "id" in body
    assert body["name"] == "resource-1"
    assert body["type"] == "demo"


def test_list_resources_returns_created_items():
    client.post("/resources", json={"name": "r1", "type": "demo"})
    client.post("/resources", json={"name": "r2", "type": "test"})

    response = client.get("/resources")

    assert response.status_code == 200
    body = response.json()

    assert len(body) == 2
    names = [item["name"] for item in body]
    assert "r1" in names
    assert "r2" in names


def test_filter_resources_by_type():
    client.post("/resources", json={"name": "r1", "type": "demo"})
    client.post("/resources", json={"name": "r2", "type": "test"})

    response = client.get("/resources", params={"type": "demo"})

    assert response.status_code == 200
    body = response.json()

    assert len(body) == 1
    assert body[0]["name"] == "r1"
    assert body[0]["type"] == "demo"


def test_create_resource_missing_required_fields_returns_400():
    response = client.post("/resources", json={})

    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid input"}


def test_create_resource_invalid_payload_returns_400():
    response = client.post(
        "/resources",
        json={"name": 123, "type": ["not", "a", "string"]},
    )

    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid input"}


def test_response_schema_contains_expected_fields():
    response = client.post(
        "/resources",
        json={"name": "schema-test", "type": "demo"},
    )

    body = response.json()

    assert set(body.keys()) == {"id", "name", "type"}

