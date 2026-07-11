"""
Example: Using __init__() and self to initialize instance attributes.
Week Six — Session One
"""

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s = Student("Abel", 20)
print(s.name, "is", s.age)
