from app import create_app


def test_health_endpoint():
    app = create_app()
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_index_endpoint_contains_keys():
    app = create_app()
    client = app.test_client()
    response = client.get("/")
    data = response.get_json()
    assert response.status_code == 200
    assert "service" in data
    assert "status" in data
    assert "environment" in data
