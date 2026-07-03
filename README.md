# Inventory Management System

A simple Flask-based Inventory Management System that provides a REST API to manage product inventory. The app includes full CRUD operations, barcode lookup via the OpenFoodFacts API, a small CLI client, and automated tests using Pytest.

## Features

- View all inventory items
- Retrieve a single item by ID
- Add new inventory items
- Update existing items
- Delete inventory items
- Lookup product details by barcode via OpenFoodFacts API
- Automated unit tests with Pytest

## Tech Stack

- Python
- Flask
- requests
- pytest

## Installation

Clone the repository and install dependencies (Pipenv recommended):

```bash
git clone <repository-url>
cd phase-5-flask-summative-assessment1
pipenv install --dev
pipenv shell
```

## Running the Application

Start the Flask server:

```bash
pipenv run flask run
```

App URL: http://127.0.0.1:5000

## Using the CLI

With the Flask server running (in a separate terminal), start the CLI:

```bash
pipenv run python cli.py
```

You'll see a menu with options to view all items, view one item, add a new item, update an item, delete an item, or search for a product by barcode using the OpenFoodFacts API.

## API Endpoints

- `GET /` — Home route with info
- `GET /inventory` — Retrieve all inventory items
- `GET /inventory/<id>` — Retrieve a single item by ID
- `POST /inventory` — Create a new item (JSON body, e.g. `{"name": "Rice 2kg", "quantity": 10, "price": 300}`)
- `PATCH /inventory/<id>` — Update an item (JSON body)
- `DELETE /inventory/<id>` — Delete an item by ID
- `GET /inventory/search/<barcode>` — Lookup product details by barcode

## Running Tests

Run the test suite with:

```bash
pipenv run pytest -v
```

Notes:
- `tests/test_external_api.py` uses mocking for external requests so tests do not require network access.
- The project uses an in-memory list for data persistence (`data.py`); tests may mutate that list during a run.

## Future Improvements

There are several ways this Inventory Management System could be improved in future versions:

- **Product Categories** — Add support for organizing inventory items into categories for easier management.
- **Advanced Search and Filtering** — Allow users to filter items by price, quantity, or category and sort results.
- **Frontend Dashboard** — Build a web-based user interface to complement the REST API and CLI.
- **Low Stock Alerts** — Notify users when an item's quantity falls below a specified threshold.
- **Persistent Database** — Replace the in-memory data store with a database such as SQLite or PostgreSQL so inventory data persists between application restarts.
- **API Documentation** — Generate interactive API documentation using Swagger/OpenAPI to make the endpoints easier to understand and test.

These enhancements would improve the application's usability, scalability, and maintainability while keeping the project focused on inventory management.