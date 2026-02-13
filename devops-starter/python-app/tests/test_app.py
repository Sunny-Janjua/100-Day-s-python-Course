from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from app import create_app


def test_health_endpoint():
    app = create_app()
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_home_page_renders():
    app = create_app()
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"TechVerse" in response.data


def test_required_pages_load():
    app = create_app()
    client = app.test_client()
    for path in ["/shop", "/cart", "/checkout", "/about", "/support", "/privacy", "/terms", "/shipping-returns", "/rewards", "/accessibility"]:
        response = client.get(path)
        assert response.status_code == 200
