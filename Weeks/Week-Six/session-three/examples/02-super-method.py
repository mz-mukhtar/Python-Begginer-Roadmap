"""
Example: Using super().__init__() in child class constructor.
Week Six — Session Three
"""

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id

s = Student("Sara", 101)
print(f"{s.name} has ID {s.student_id}")
