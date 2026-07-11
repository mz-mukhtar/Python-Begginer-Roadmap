"""
Exercise 4 Solution: Product Class
Week Six — Session One
"""

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def total_value(self):
        return self.price * self.quantity

p = Product("Mouse", 25, 4)
print("Total value:", p.total_value())
