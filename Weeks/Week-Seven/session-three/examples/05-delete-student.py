"""
Example: Deleting student by ID.
Week Seven — Session Three
"""

class Student:
    def __init__(self, sid, name):
        self.sid = sid
        self.name = name

class StudentManager:
    def __init__(self):
        self.students = [Student(1, "Abel"), Student(2, "Sara")]

    def delete_student(self, sid):
        for i, s in enumerate(self.students):
            if s.sid == sid:
                del self.students[i]
                return True
        return False

mgr = StudentManager()
mgr.delete_student(1)
print("Remaining count:", len(mgr.students))
