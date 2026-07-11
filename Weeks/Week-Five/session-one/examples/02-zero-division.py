"""
Example: Handling ZeroDivisionError.
Week Five — Session One
"""

try:
    result = 100 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
