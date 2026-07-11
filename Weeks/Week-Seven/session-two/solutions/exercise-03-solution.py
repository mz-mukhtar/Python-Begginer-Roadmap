"""
Exercise 3 Solution: Convert Student to Dict
Week Seven — Session Two
"""

class Student:
    def __init__(self, sid, name):
        self.sid = sid
        self.name = name
    def to_dict(self): return {"sid": self.sid, "name": self.name}
print(Student(1, "Abel").to_dict())
