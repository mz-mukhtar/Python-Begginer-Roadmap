"""
Exercise 1 Solution: Person and Student
Week Six — Session Three
"""

class Person:
    def __init__(self, name): self.name = name
class Student(Person): pass
print(Student("Abel").name)
