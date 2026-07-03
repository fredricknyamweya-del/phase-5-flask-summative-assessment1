import pytest
from unittest.mock import patch, MagicMock
from external_api import fetch_product

def test_fetch_product_success():
    fake_response = MagicMock()
    fake_response.status_code = 200
    fake_response.json.return_value = {
        "status": 1,
        "product": {
            "product_name": "Test Product",
            "brands": "Test Brand",
            "ingredients_text": "Test Ingredients"
        }
    }

    with patch('external_api.requests.get', return_value=fake_response):
        result = fetch_product("1234567890123")
        assert result is not None
        assert result["product_name"] == "Test Product"
        assert result["brands"] == "Test Brand"
        assert result["ingredients_text"] == "Test Ingredients"

def test_fetch_product_not_found():
    fake_response = MagicMock()
    fake_response.status_code = 200
    fake_response.json.return_value = {"status": 0}

    with patch('external_api.requests.get', return_value=fake_response):
        result = fetch_product("000000000")
        assert result is None