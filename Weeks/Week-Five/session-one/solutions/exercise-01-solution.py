"""
Exercise 1 Solution: Safe Age Input
Week Five — Session One
"""

try:
    age = int(input("Enter age: "))
    print("Age recorded:", age)
except ValueError:
    print("Invalid age entered.")
