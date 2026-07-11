"""
Exercise 3 Solution: Update Object Information
Week Six — Session Two
"""

class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major

s = Student("Abel", "EE")
s.major = "CS"
print("Updated major:", s.major)
