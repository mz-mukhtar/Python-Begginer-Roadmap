"""
Exercise 2 Solution: Validate Student Age
Week Seven — Session Two
"""

class Student:
    def __init__(self, name, age):
        if age < 16: raise ValueError("Invalid age")
        self.name = name
        self.age = age
print("Validation rule set.")
