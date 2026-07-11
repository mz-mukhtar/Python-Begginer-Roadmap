"""
Exercise 2 Solution: Vehicle and Car
Week Six — Session Three
"""

class Vehicle:
    def __init__(self, brand): self.brand = brand
class Car(Vehicle):
    def __init__(self, brand, doors):
        super().__init__(brand)
        self.doors = doors
print(Car("Toyota", 4).brand)
