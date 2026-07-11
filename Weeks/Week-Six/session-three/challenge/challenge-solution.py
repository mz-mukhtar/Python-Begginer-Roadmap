"""
Challenge Solution: Object-Oriented Student Management System
Week Six — Session Three
"""

class Student:
    def __init__(self, sid, name):
        self.sid = sid
        self.name = name

class StudentSystem:
    def __init__(self):
        self.students = []
    def add(self, sid, name):
        self.students.append(Student(sid, name))
        print("Registered:", name)

system = StudentSystem()
system.add(101, "Abel")
system.add(102, "Sara")
