"""
Exercise 3 Solution: Search Student by ID
Week Seven — Session Three
"""

class Student:
    def __init__(self, sid, name): self.sid = sid; self.name = name
class StudentManager:
    def __init__(self): self.students = [Student(10, "Abel")]
    def find(self, sid):
        for s in self.students:
            if s.sid == sid: return s
        return None
m = StudentManager()
print(m.find(10).name)
