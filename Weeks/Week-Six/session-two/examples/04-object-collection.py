"""
Example: Iterating over objects inside a manager.
Week Six — Session Two
"""

class Student:
    def __init__(self, name):
        self.name = name

students = [Student("Abel"), Student("Sara")]
for s in students:
    print(f"Student entry: {s.name}")
