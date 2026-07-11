"""
Exercise 5 Solution: Improve Error Messages
Week Five — Session Three
"""

try:
    val = int("invalid")
except ValueError:
    print("Friendly Error: Please check that your input contains only numbers.")
