"""
Exercise 2 Solution: Safe Division
Week Five — Session One
"""

try:
    res = 50 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")
