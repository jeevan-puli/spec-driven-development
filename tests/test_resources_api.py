import logging

logger = logging.getLogger(__name__)

from fastapi.testclient import TestClient

from app.main import app, resources

client = TestClient(app)


def setup_function():
    # Ensure deterministic tests by clearing in-memory storage
    resources.clear()


def test_create_resource_success():
    logger.info("Creating resource with valid payload")

    response = client.post(
        "/resources",
        json={"name": "resource-1", "type": "demo"},
    )

    logger.info("Create response status=%s body=%s", response.status_code, response.json())

    assert response.status_code == 200
    body = response.json()

    assert "id" in body
    assert body["name"] == "resource-1"
    assert body["type"] == "demo"


def test_list_resources_returns_created_items():
    logger.info("Creating multiple resources for list test")

    client.post("/resources", json={"name": "r1", "type": "demo"})
    client.post("/resources", json={"name": "r2", "type": "test"})

    logger.info("Fetching all resources")

    response = client.get("/resources")
    logger.info("List response status=%s body=%s", response.status_code, response.json())

    assert response.status_code == 200
    body = response.json()

    assert len(body) == 2
    names = [item["name"] for item in body]
    assert "r1" in names
    assert "r2" in names


def test_filter_resources_by_type():
    logger.info("Creating resources with different types")

    client.post("/resources", json={"name": "r1", "type": "demo"})
    client.post("/resources", json={"name": "r2", "type": "test"})

    logger.info("Filtering resources by type=demo")

    response = client.get("/resources", params={"type": "demo"})
    logger.info("Filter response status=%s body=%s", response.status_code, response.json())

    assert response.status_code == 200
    body = response.json()

    assert len(body) == 1
    assert body[0]["name"] == "r1"
    assert body[0]["type"] == "demo"


def test_create_resource_missing_required_fields_returns_400():
    logger.info("Creating resource with missing required fields")

    response = client.post("/resources", json={})
    logger.info("Validation response status=%s body=%s", response.status_code, response.json())

    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid input"}


def test_create_resource_invalid_payload_returns_400():
    logger.info("Creating resource with invalid payload types")

    response = client.post(
        "/resources",
        json={"name": 123, "type": ["not", "a", "string"]},
    )

    logger.info("Invalid payload response status=%s body=%s", response.status_code, response.json())

    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid input"}


def test_response_schema_contains_expected_fields():
    logger.info("Validating response schema for created resource")

    response = client.post(
        "/resources",
        json={"name": "schema-test", "type": "demo"},
    )

    body = response.json()
    logger.info("Schema validation response body=%s", body)

    assert set(body.keys()) == {"id", "name", "type"}


def test_list_resources_returns_empty_list_when_no_resources_exist():
    logger.info("Listing resources when no resources exist")

    response = client.get("/resources")
    logger.info("Empty list response status=%s body=%s", response.status_code, response.json())

    assert response.status_code == 200
    assert response.json() == []
