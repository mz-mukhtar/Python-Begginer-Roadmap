"""
Exercise 5 Solution: Multiple Objects
Week Six — Session One
"""

class Student:
    def __init__(self, name):
        self.name = name

roster = [Student("Abel"), Student("Sara"), Student("Mahi")]
for s in roster:
    print(s.name)
