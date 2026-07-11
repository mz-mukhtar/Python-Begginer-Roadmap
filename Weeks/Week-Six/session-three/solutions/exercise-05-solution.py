"""
Exercise 5 Solution: Inheritance Review
Week Six — Session Three
"""

class Person: pass
class Student(Person): pass
s = Student()
print("Is Person instance:", isinstance(s, Person))
