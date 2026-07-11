"""
Exercise 2 Solution: Create Product Functions
Week Three — Session Three
"""

def create_product(name, price):
    return {"name": name, "price": price}

def display_product(product):
    print(f"{product['name']} - ${product['price']}")

p = create_product("Monitor", 200)
display_product(p)
