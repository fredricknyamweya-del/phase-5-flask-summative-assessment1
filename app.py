from flask import Flask, jsonify
from data import inventory

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return jsonify({"message": "Welcome to the Inventory Management System API!",
                    "endpoints": {
                        "GET /inventory": "View all inventory items",
                        "GET /inventory/<int:item_id>": "View a single inventory item by ID"
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



if __name__ == '__main__':
    app.run(debug=True)