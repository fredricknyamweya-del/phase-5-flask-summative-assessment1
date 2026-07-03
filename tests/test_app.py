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