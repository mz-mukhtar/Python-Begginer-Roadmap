"""
Exercise 2 Solution: Add Student Record
Week Seven — Session Three
"""

class Student:
    def __init__(self, sid, name): self.sid = sid; self.name = name
class StudentManager:
    def __init__(self): self.students = []
    def add(self, s):
        if any(x.sid == s.sid for x in self.students): return False
        self.students.append(s); return True
m = StudentManager()
print("Added:", m.add(Student(1, "Abel")))
