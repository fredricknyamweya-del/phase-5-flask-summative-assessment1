from external_api import fetch_product

# Real barcodes to merge the inventory with actual OpenFoodFacts data
barcodes = [
    "3017620422003",   # Nutella
    "5059319023533",   # Rice Krispies
    "5000442007594",   # Olive oil
    "3760049790214",   # Pain De Mie Bio (bread)
]

inventory = []

for index, barcode in enumerate(barcodes, start=1):
    product = fetch_product(barcode)
    if product:
        inventory.append({
            "id": index,
            "name": product["product_name"],
            "quantity": 10,
            "price": 100.0
        })