"""
Exercise 4 Solution: Read Student CSV
Week Four — Session Three
"""

import csv
with open("grades.csv", "r") as f:
    for row in csv.reader(f):
        print(row)
