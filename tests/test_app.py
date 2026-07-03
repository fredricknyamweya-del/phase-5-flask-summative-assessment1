import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200

def test_get_all_inventory(client):
    response = client.get('/inventory')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)

def test_get_inventory_item_valid(client):
    response = client.get('/inventory/1')
    assert response.status_code == 200

def test_get_inventory_item_invalid(client):
    response = client.get('/inventory/999')
    assert response.status_code == 404

def test_create_item_success(client):
    payload = {"name": "Test Item", "quantity": 5, "price": 10.5}
    response = client.post("/inventory", json=payload)
    assert response.status_code == 201
    data = response.get_json()
    assert "id" in data
    assert data["name"] == "Test Item"

def test_create_item_missing_name(client):
    payload = {"quantity": 5, "price": 10.5}
    response = client.post("/inventory", json=payload)
    assert response.status_code == 400

def test_update_item_success(client):
    payload = {"price": 999}
    response = client.patch("/inventory/1", json=payload)
    assert response.status_code == 200
    data = response.get_json()
    assert data["price"] == 999

def test_update_item_not_found(client):
    payload = {"price": 123}
    response = client.patch("/inventory/999", json=payload)
    assert response.status_code == 404

def test_delete_item_success(client):
    # create a new item first
    payload = {"name": "Temp Item", "quantity": 1, "price": 1.0}
    create_response = client.post("/inventory", json=payload)
    assert create_response.status_code == 201
    new_item = create_response.get_json()
    new_id = new_item["id"]

    # now delete it
    delete_response = client.delete(f"/inventory/{new_id}")
    assert delete_response.status_code == 200

def test_delete_item_not_found(client):
    response = client.delete("/inventory/999")
    assert response.status_code == 404
