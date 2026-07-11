"""
Example: Updating student details by ID.
Week Seven — Session Three
"""

class Student:
    def __init__(self, sid, name, major):
        self.sid = sid
        self.name = name
        self.major = major

class StudentManager:
    def __init__(self):
        self.students = [Student(1, "Abel", "EE")]

    def update_student(self, sid, new_major):
        for s in self.students:
            if s.sid == sid:
                s.major = new_major
                return True
        return False

mgr = StudentManager()
mgr.update_student(1, "CS")
print("Updated major:", mgr.students[0].major)
