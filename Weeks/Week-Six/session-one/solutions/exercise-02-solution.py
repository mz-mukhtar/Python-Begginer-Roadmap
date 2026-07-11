"""
Exercise 2 Solution: Car Class
Week Six — Session One
"""

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def start_engine(self):
        print(f"The {self.brand} {self.model} engine started!")

c = Car("Toyota", "RAV4")
c.start_engine()
