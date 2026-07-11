"""
Exercise 3 Solution: Create Grade CSV
Week Four — Session Three
"""

import csv
with open("grades.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["Student", "Grade"])
    w.writerow(["Abel", "A"])
print("Grades CSV saved.")
