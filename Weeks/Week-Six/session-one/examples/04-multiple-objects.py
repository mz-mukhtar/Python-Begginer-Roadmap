"""
Example: Creating multiple independent objects from one class.
Week Six — Session One
"""

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

c1 = Car("Toyota", "Corolla")
c2 = Car("Honda", "Civic")
print(c1.brand, "vs", c2.brand)
