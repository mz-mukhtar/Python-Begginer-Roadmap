"""
Example: Storing multiple objects inside a list.
Week Six — Session One
"""

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

students = [Student("Abel", 20), Student("Sara", 19)]
for s in students:
    print(s.name)
