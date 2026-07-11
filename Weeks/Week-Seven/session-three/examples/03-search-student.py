"""
Example: Searching student by ID.
Week Seven — Session Three
"""

class Student:
    def __init__(self, sid, name):
        self.sid = sid
        self.name = name

class StudentManager:
    def __init__(self):
        self.students = [Student(101, "Abel"), Student(102, "Sara")]

    def find_by_id(self, sid):
        for s in self.students:
            if s.sid == sid:
                return s
        return None

mgr = StudentManager()
found = mgr.find_by_id(101)
print("Found:", found.name if found else "None")
