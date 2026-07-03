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

App URL:

http://127.0.0.1:5000

## API Endpoints

- `GET /` — Home route with info    
- `GET /inventory` — Retrieve all inventory items
- `GET /inventory/<id>` — Retrieve a single item by ID
- `POST /inventory` — Create a new item (JSON body)
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

