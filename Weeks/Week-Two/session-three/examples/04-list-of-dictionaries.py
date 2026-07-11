"""
Example: List containing multiple dictionary records.
Week Two — Session Three
"""

students = [
    {"name": "Abel", "age": 20},
    {"name": "Sara", "age": 19}
]

for student in students:
    print(student["name"], "is", student["age"], "years old.")
