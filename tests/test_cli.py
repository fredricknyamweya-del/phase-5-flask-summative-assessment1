from unittest.mock import patch, MagicMock
from cli import view_all_items, view_one_item, add_item


def test_view_all_items(capsys):
    fake_response = MagicMock()
    fake_response.status_code = 200
    fake_response.json.return_value = [
        {"id": 1, "name": "Nutella", "quantity": 10, "price": 100.0}
    ]

    with patch("cli.requests.get", return_value=fake_response):
        view_all_items()

    captured = capsys.readouterr()
    assert "Nutella" in captured.out


def test_view_one_item_found(capsys):
    fake_response = MagicMock()
    fake_response.status_code = 200
    fake_response.json.return_value = {
        "id": 1,
        "name": "Nutella",
        "quantity": 10,
        "price": 100.0,
    }

    with patch("cli.requests.get", return_value=fake_response), patch("builtins.input", return_value="1"):
        view_one_item()

    captured = capsys.readouterr()
    assert "Nutella" in captured.out


def test_view_one_item_not_found(capsys):
    fake_response = MagicMock()
    fake_response.status_code = 404
    fake_response.json.return_value = {"error": "Item not found"}

    with patch("cli.requests.get", return_value=fake_response), patch("builtins.input", return_value="99"):
        view_one_item()

    captured = capsys.readouterr()
    # Match the CLI’s actual print message, not the JSON
    assert "not found" in captured.out


def test_add_item_success(capsys):
    fake_response = MagicMock()
    fake_response.status_code = 201
    fake_response.json.return_value = {
        "id": 5,
        "name": "Rice",
        "quantity": 20,
        "price": 300.0,
    }

    with patch("cli.requests.post", return_value=fake_response), \
         patch("builtins.input", side_effect=["Rice", "20", "300.0"]):
        add_item()

    captured = capsys.readouterr()
    assert "Rice" in captured.out


def test_add_item_failure_invalid_quantity(capsys):
    fake_response = MagicMock()
    fake_response.status_code = 400
    fake_response.json.return_value = {"error": "Invalid input"}

    # Simulate user typing: name="Rice", quantity="abc" (bad), price="300.0"
    with patch("cli.requests.post", return_value=fake_response), \
         patch("builtins.input", side_effect=["Rice", "abc", "300.0"]):
        add_item()

    captured = capsys.readouterr()
    # Match the actual CLI error message
    assert "must be an integer" in captured.out
