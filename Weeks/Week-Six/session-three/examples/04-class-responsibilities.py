"""
Example: Clean separation of model and file manager responsibilities.
Week Six — Session Three
"""

class Student:
    def __init__(self, name):
        self.name = name

class StudentRepository:
    def save(self, students):
        print(f"Saving {len(students)} student records.")
