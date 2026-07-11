"""
Exercise 5 Solution: Test Model Methods
Week Seven — Session Two
"""

class Student:
    def __init__(self, sid, name):
        self.sid = sid
        self.name = name
    def to_dict(self): return {"sid": self.sid, "name": self.name}
s = Student(5, "Jon")
assert s.to_dict()["sid"] == 5
print("Model test passed.")
