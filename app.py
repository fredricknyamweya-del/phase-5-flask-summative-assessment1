from flask import Flask, jsonify, request
from data import inventory
from external_api import fetch_product

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return jsonify({"message": "Welcome to the Inventory Management System API!",
                    "endpoints": {
                        "GET /inventory": "View all inventory items",
                        "GET /inventory/<int:item_id>": "View a single inventory item by ID",
                        "POST /inventory": "Add a new inventory item",
                        "PATCH /inventory/<int:item_id>": "Update an existing inventory item",
                        "DELETE /inventory/<int:item_id>": "Delete an inventory item by ID"
                    }
    })
    
#Get all items in the inventory
@app.route('/inventory', methods=['GET'])
def get_inventory():
    return jsonify(inventory), 200

#Get a single item in the inventory by ID
@app.route('/inventory/<int:item_id>', methods=['GET'])
def get_inventory_item(item_id):
    item = next((item for item in inventory if item["id"] == item_id), None)
    if item:
        return jsonify(item), 200
    else:
        return jsonify({"error": "Item not found"}), 404

#POST new item to the inventory
@app.route('/inventory', methods=['POST'])
def create_inventory_item():
    data = request.get_json()
    
    if not data or "name" not in data:
        return jsonify({"error": "Missing 'name' field"}), 400
    
    new_id = inventory[-1]["id"] + 1 if inventory else 1
    
    new_item = {
        "id": new_id,
        "name": data["name"],
        "quantity": data.get("quantity", 0),
        "price": data.get("price", 0.0)
    }
    
    inventory.append(new_item)
    return jsonify(new_item), 201

@app.route('/inventory/<int:item_id>', methods=['PATCH'])
def update_inventory_item(item_id):
    item =next((item for item in inventory if item["id"] == item_id), None)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    
    updates = request.get_json()
    if not updates:
        return jsonify({"error": "No update data provided"}), 400
    
    item.update(updates)
    return jsonify(item), 200

@app.route('/inventory/<int:item_id>', methods=['DELETE'])
def delete_inventory_item(item_id):
    item = next((item for item in inventory if item["id"] == item_id), None)
    if not item:
        return jsonify({"error": "Item not found"}), 404

    inventory.remove(item)
    return jsonify({"message": f"Item {item_id} deleted successfully"}), 200

@app.route("/inventory/search/<barcode>", methods=['GET'])
def search_inventory(barcode):
    product = fetch_product(barcode)
    if product is None:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product), 200

@app.route("/inventory/search/<barcode>", methods=['POST'])
def add_product_to_inventory(barcode):
    """
    Fetch the product details from the external API using the barcode and add it to the inventory with default values.
    """
    
    product = fetch_product(barcode)
    if product is None:
        return jsonify({"error": "Product not found"}), 404
    
    new_id = max([item["id"] for item in inventory], default=0) + 1
    
    new_item = {
        "id": new_id,
        "name": product.get("product_name", "Unknown Product"),
        "quantity": 0,
        "price": 0.0
    }
    inventory.append(new_item)
    return jsonify(new_item), 201

if __name__ == '__main__':
    app.run(debug=True)