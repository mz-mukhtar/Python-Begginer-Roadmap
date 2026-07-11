"""
Exercise 4 Solution: Update Student Major
Week Seven — Session Three
"""

class Student:
    def __init__(self, sid, major): self.sid = sid; self.major = major
class StudentManager:
    def __init__(self): self.students = [Student(1, "EE")]
    def update_major(self, sid, new_major):
        for s in self.students:
            if s.sid == sid: s.major = new_major; return True
        return False
m = StudentManager(); m.update_major(1, "CS")
print(m.students[0].major)
