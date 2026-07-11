"""
Exercise 4 Solution: Product Categories
Week Six — Session Three
"""

class Product:
    def __init__(self, name): self.name = name
class ElectronicProduct(Product):
    def __init__(self, name, warranty_years):
        super().__init__(name)
        self.warranty_years = warranty_years
print(ElectronicProduct("TV", 2).warranty_years)
