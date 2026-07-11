"""
Challenge Solution: In-Memory Student Management Controller
Week Seven — Session Three
"""

class Student:
    def __init__(self, sid, name, major):
        self.sid = sid
        self.name = name
        self.major = major

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        for s in self.students:
            if s.sid == student.sid:
                return False, "Duplicate ID"
        self.students.append(student)
        return True, "Added successfully"

    def get_all(self):
        return self.students

    def delete_student(self, sid):
        for i, s in enumerate(self.students):
            if s.sid == sid:
                del self.students[i]
                return True
        return False

mgr = StudentManager()
mgr.add_student(Student(101, "Abel", "CS"))
mgr.add_student(Student(102, "Sara", "EE"))
print("Total students:", len(mgr.get_all()))
