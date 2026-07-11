"""
Example: StudentManager class coordinating a collection.
Week Six — Session Two
"""

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student_obj):
        self.students.append(student_obj)
        print("Added:", student_obj.name)
