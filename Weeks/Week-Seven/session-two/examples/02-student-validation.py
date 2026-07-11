"""
Example: Adding validation to constructor or helper method.
Week Seven — Session Two
"""

class Student:
    def __init__(self, student_id, name, age):
        if age <= 0:
            raise ValueError("Age must be positive")
        self.student_id = student_id
        self.name = name
        self.age = age

print("Student model validation ready.")
