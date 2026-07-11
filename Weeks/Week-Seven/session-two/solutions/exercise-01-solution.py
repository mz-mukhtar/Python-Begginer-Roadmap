"""
Exercise 1 Solution: Instantiate Student Model
Week Seven — Session Two
"""

class Student:
    def __init__(self, sid, name):
        self.sid = sid
        self.name = name
print(Student(1, "Abel").name)
