# API Endpoints Documentation

Detailed reference for all routes in the Inventory Management System.

---

## GET /

Returns the home route.

**Response 200:**

```json
{"message": "Welcome to the Inventory System"}
```

---

## GET /inventory

Returns all items in the inventory.

**Response 200:**

```json
[
  {"id": 1, "name": "Milk 500ml", "quantity": 24, "price": 60.0},
  {"id": 2, "name": "White Bread 400g", "quantity": 12, "price": 65.0}
]
```

---

## GET /inventory/<id>

Returns a single item by ID.

**Response 200 (valid ID):**

```json
{"id": 1, "name": "Milk 500ml", "quantity": 24, "price": 60.0}
```

**Response 404 (invalid ID):**

```json
{"error": "Item not found"}
```

---

## POST /inventory

Creates a new item. Requires JSON body.

**Request Body Example:**

```json
{"name": "Rice 2kg", "quantity": 10, "price": 300}
```

**Response 201:**

```json
{"id": 3, "name": "Rice 2kg", "quantity": 10, "price": 300}
```

**Response 400 (missing name):**

```json
{"error": "Name is required"}
```

---

## PATCH /inventory/<id>

Updates an existing item. Requires JSON body with fields to update.

**Request Body Example:**

```json
{"price": 999}
```

**Response 200 (valid ID):**

```json
{"id": 1, "name": "Milk 500ml", "quantity": 24, "price": 999}
```

**Response 404 (invalid ID):**

```json
{"error": "Item not found"}
```

---

## DELETE /inventory/<id>

Deletes an item by ID.

**Response 200 (valid ID):**

```json
{"message": "Item deleted successfully"}
```

**Response 404 (invalid ID):**

```json
{"error": "Item not found"}
```

---

## GET /inventory/search/<barcode>

Looks up product details from the external API (OpenFoodFacts).

**Response 200 (found):**

```json
{
  "product_name": "Nutella",
  "brands": "Ferrero",
  "ingredients_text": "Sugar, palm oil, hazelnuts, cocoa, skim milk..."
}
```

**Response 404 (not found):**

```json
{"error": "Product not found"}
```