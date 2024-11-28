import requests
import json

# Base URL of the API
BASE_URL = "http://127.0.0.1:5000/products"

# Function to create a new product
def create_product(name, description, price):
    data = {
        "name": name,
        "description": description,
        "price": price
    }
    response = requests.post(BASE_URL, json=data)
    if response.status_code == 201:
        print("Product created successfully:", response.json())
    else:
        print("Failed to create product:", response.status_code, response.json())

# Function to fetch all products
def get_products():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        print("Products retrieved successfully:")
        print(json.dumps(response.json(), indent=4))
    else:
        print("Failed to retrieve products:", response.status_code)

if __name__ == "__main__":
    # Test creating a product
    print("Creating a new product...")
    create_product("Laptop", "A high-performance laptop", 999.99)
    
    # Test retrieving all products
    print("\nFetching all products...")
    get_products()
