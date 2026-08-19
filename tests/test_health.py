"""TommyTech test suite."""

import pytest
from fastapi.testclient import TestClient


def test_health_check(client: TestClient):
    """Verify the health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "version" in data


def test_root_endpoint(client: TestClient):
    """Verify the root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data


@pytest.fixture
def client():
    """Create a test client for the FastAPI app."""
    from src.main import app

    from fastapi.testclient import TestClient

    return TestClient(app)
