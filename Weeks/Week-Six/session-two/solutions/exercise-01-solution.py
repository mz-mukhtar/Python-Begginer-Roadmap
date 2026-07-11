"""
Exercise 1 Solution: Add Objects to a List
Week Six — Session Two
"""

class Student:
    def __init__(self, name):
        self.name = name

roster = [Student("Abel"), Student("Sara")]
print(len(roster), "students created.")
