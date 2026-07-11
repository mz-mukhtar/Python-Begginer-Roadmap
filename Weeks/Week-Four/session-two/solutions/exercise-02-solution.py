"""
Exercise 2 Solution: Read Notes
Week Four — Session Two
"""

with open("student_name.txt", "r") as f:
    print(f.read().strip())
