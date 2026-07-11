"""
Challenge Solution: Course Registration Class
Week Six — Session One
"""

class Course:
    def __init__(self, code, title, capacity):
        self.code = code
        self.title = title
        self.capacity = capacity
        self.enrolled = []

    def enroll(self, student_name):
        if len(self.enrolled) < self.capacity:
            self.enrolled.append(student_name)
            print(f"Enrolled {student_name} in {self.code}")
        else:
            print(f"Course {self.code} is full!")

c = Course("CS101", "Python Basics", 2)
c.enroll("Abel")
c.enroll("Sara")
c.enroll("Jon")
