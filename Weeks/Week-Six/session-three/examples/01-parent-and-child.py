"""
Example: Basic parent and child inheritance.
Week Six — Session Three
"""

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    pass

s = Student("Abel")
print("Student inherited name:", s.name)
