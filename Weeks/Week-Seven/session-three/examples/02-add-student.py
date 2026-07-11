"""
Example: Adding student with duplicate ID check.
Week Seven — Session Three
"""

class Student:
    def __init__(self, sid, name):
        self.sid = sid
        self.name = name

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        for s in self.students:
            if s.sid == student.sid:
                print("Error: Student ID already exists!")
                return False
        self.students.append(student)
        return True

m = StudentManager()
m.add_student(Student(1, "Abel"))
m.add_student(Student(1, "Duplicate"))
