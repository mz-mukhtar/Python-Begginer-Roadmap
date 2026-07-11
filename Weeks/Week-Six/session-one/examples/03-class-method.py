"""
Example: Adding methods to a class.
Week Six — Session One
"""

class Student:
    def __init__(self, name, department):
        self.name = name
        self.department = department

    def display(self):
        print(f"Student: {self.name} | Dept: {self.department}")

s = Student("Sara", "EE")
s.display()
