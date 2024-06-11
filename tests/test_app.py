from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "Product 1" in response.text

def test_add_to_cart():
    response = client.post("/add_to_cart/", data={"product_id": 1})
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "Product 1" in response.text

def test_view_cart():
    response = client.get("/cart")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "Total Price" in response.text
