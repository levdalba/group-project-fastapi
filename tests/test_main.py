from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_root() -> None:
    """Test the root endpoint returns a welcome message."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to FastAPI!"}


def test_create_item() -> None:
    """Test creating an item with name and price."""
    response = client.post("/items/", json={"name": "apple", "price": 1.99})
    assert response.status_code == 200
    assert response.json() == {"name": "apple", "price": 1.99}
