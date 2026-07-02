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

def main_menu():
    while True:
        print("=== Inventory Management CLI ===")
        print("1. View all items")
        print("2. View one item by ID")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            view_all_items()
        elif choice == "2":
            view_one_item()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    main_menu()
