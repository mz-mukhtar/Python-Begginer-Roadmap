"""
Example: Production-ready Student data model class.
Week Seven — Session Two
"""

class Student:
    def __init__(self, student_id, name, age, major):
        self.student_id = int(student_id)
        self.name = str(name).strip()
        self.age = int(age)
        self.major = str(major).strip()
