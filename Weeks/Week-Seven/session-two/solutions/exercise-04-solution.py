"""
Exercise 4 Solution: Load Student from Dict
Week Seven — Session Two
"""

class Student:
    def __init__(self, sid, name):
        self.sid = sid
        self.name = name
    @classmethod
    def from_dict(cls, d): return cls(d["sid"], d["name"])
s = Student.from_dict({"sid": 10, "name": "Sara"})
print(s.name)
