import requests

BASE_URL = "http://127.0.0.1:5000"

def view_all_items():
    response = requests.get(f"{BASE_URL}/inventory")
    if response.status_code != 200:
        print("Error: Could not fetch inventory.")
        return

    items = response.json()
    print("\n--- Inventory ---")
    for item in items:
        print(f"ID: {item['id']} | Name: {item['name']} | Quantity: {item['quantity']} | Price: {item['price']}")
    print("-----------------\n")

def view_one_item():
    item_id = input("Enter the item ID: ")
    response = requests.get(f"{BASE_URL}/inventory/{item_id}")

    if response.status_code == 404:
        print(f"Item with ID {item_id} not found.\n")
        return
    elif response.status_code != 200:
        print("Error: Could not fetch item.\n")
        return

    item = response.json()
    print("\n--- Item Details ---")
    print(f"ID: {item['id']}")
    print(f"Name: {item['name']}")
    print(f"Quantity: {item['quantity']}")
    print(f"Price: {item['price']}")
    print("--------------------\n")

def add_item():
    name = input("Enter item name: ")
    quantity = input("Enter quantity: (integer) ")
    price = input("Enter price: (float): ")
    
    try:
        quantity = int(quantity)
        price = float(price)
    except ValueError:
        print("Error: Quantity must be an integer and price must be a float.\n")
        return

    payload = {
        "name": name,
        "quantity": int(quantity),
        "price": float(price)
    }

    response = requests.post(f"{BASE_URL}/inventory", json=payload)
    if response.status_code == 201:
        item = response.json()
        print("\nItem added successfully:")
        print(f"ID: {item['id']} | Name: {item['name']} | Quantity: {item['quantity']} | Price: {item['price']}\n")
    else:
        print("Error: Could not add item.\n")

def main_menu():
    while True:
        print("=== Inventory Management CLI ===")
        print("1. View all items")
        print("2. View one item by ID")
        print("3. Add new item")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            view_all_items()
        elif choice == "2":
            view_one_item()
        elif choice == "3":
            add_item()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    main_menu()
