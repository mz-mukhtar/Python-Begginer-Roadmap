"""
Exercise 2 Solution: Search Objects
Week Six — Session Two
"""

class Student:
    def __init__(self, sid, name):
        self.sid = sid
        self.name = name

roster = [Student(1, "Abel"), Student(2, "Sara")]
for s in roster:
    if s.sid == 2:
        print("Found:", s.name)
