"""
Example: Loading structured data from JSON.
Week Four — Session Three
"""

import json

with open("students.json", "r") as f:
    students = json.load(f)

for s in students:
    print(s["name"], "studies", s["major"])
