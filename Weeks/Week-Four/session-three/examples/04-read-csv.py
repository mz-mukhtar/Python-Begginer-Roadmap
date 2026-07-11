"""
Example: Reading rows from a CSV file.
Week Four — Session Three
"""

import csv

with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print("Row:", row)
