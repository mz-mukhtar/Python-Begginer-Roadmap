"""
Exercise 1 Solution: Student Class
Week Six — Session One
"""

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s = Student("Abel", 20)
print(s.name, s.age)
