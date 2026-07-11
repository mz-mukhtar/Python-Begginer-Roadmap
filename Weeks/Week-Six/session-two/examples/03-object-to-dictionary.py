"""
Example: Converting an object to dictionary for JSON saving.
Week Six — Session Two
"""

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def to_dict(self):
        return {"name": self.name, "age": self.age}

s = Student("Abel", 20)
print(s.to_dict())
