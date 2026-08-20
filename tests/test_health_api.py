from fastapi.testclient import TestClient

from app.api.health import app


client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["service"] == "pulse-monitor"


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200

    data = response.json()

    assert data["service"] == "pulse-monitor"
    assert "status" in data
    assert "checked_at" in data
    assert "uptime_hours" in data
    assert "checks" in data


def test_health_contains_expected_checks():
    response = client.get("/health")

    data = response.json()

    assert "cpu" in data["checks"]
    assert "memory" in data["checks"]
    assert "disk" in data["checks"]


def test_metrics_endpoint():
    response = client.get("/metrics")

    assert response.status_code == 200
    assert "system_cpu_usage_percent" in response.text
    assert "system_memory_usage_percent" in response.text
    assert "system_disk_usage_percent" in response.text
    assert "system_uptime_hours" in response.text