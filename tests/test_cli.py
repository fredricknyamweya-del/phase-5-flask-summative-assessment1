from unittest.mock import patch, MagicMock
from cli import view_all_items, view_one_item, update_item, delete_item


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


def test_update_item_success(capsys):
    fake_response = MagicMock()
    fake_response.status_code = 200
    fake_response.json.return_value = {
        "id": 1,
        "name": "Nutella",
        "quantity": 10,
        "price": 150.0,  # updated price
    }

    with patch("cli.requests.patch", return_value=fake_response), \
         patch("builtins.input", side_effect=["1", "price", "150.0"]):
        update_item()

    captured = capsys.readouterr()
    assert "Nutella" in captured.out
    assert "150.0" in captured.out


def test_update_item_invalid_field(capsys):
    with patch("builtins.input", side_effect=["1", "name", "something"]):
        update_item()

    captured = capsys.readouterr()
    # Match the CLI’s actual invalid field message
    assert "Invalid field" in captured.out


def test_delete_item_success(capsys):
    fake_response = MagicMock()
    fake_response.status_code = 200
    fake_response.json.return_value = {"message": "Item deleted"}

    with patch("cli.requests.delete", return_value=fake_response), \
         patch("builtins.input", return_value="1"):
        delete_item()

    captured = capsys.readouterr()
    assert "deleted" in captured.out


def test_delete_item_not_found(capsys):
    fake_response = MagicMock()
    fake_response.status_code = 404
    fake_response.json.return_value = {"error": "Item not found"}

    with patch("cli.requests.delete", return_value=fake_response), \
         patch("builtins.input", return_value="99"):
        delete_item()

    captured = capsys.readouterr()
    assert "not found" in captured.out
