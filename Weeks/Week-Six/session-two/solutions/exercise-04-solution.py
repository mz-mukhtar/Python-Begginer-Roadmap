"""
Exercise 4 Solution: Convert Object to Dictionary
Week Six — Session Two
"""

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def to_dict(self):
        return {"name": self.name, "price": self.price}

p = Product("Keyboard", 45)
print(p.to_dict())
