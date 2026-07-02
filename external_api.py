import requests

def fetch_product(barcode: str):
    """
    Fetch product details from OpenFoodFacts API using the provided barcode.
    Returns a dictionary with product_name, product_quantity, and ingridients_text if the product is found, otherwise returns None.
    """
    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"
    headers = {
        "User-Agent": "InventoryManagementSystem/1.0 (https://github.com/fredricknyamweya-del/phase-5-flask-summative-assessment1/commits/main/)"
    }
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return None

    data = response.json()

    if data.get("status") != 1:
        return None
    
    product = data.get("product", {})
    return {
        "product_name": product.get("product_name"),
        "brands": product.get("brands"),
        "ingredients_text": product.get("ingredients_text")
    }