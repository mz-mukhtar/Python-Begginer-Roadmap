"""
Exercise 5 Solution: Remove Student Record
Week Seven — Session Three
"""

class Student:
    def __init__(self, sid): self.sid = sid
class StudentManager:
    def __init__(self): self.students = [Student(1), Student(2)]
    def delete(self, sid):
        self.students = [s for s in self.students if s.sid != sid]
m = StudentManager(); m.delete(1)
print(len(m.students))
