"""
Example: Converting JSON data to CSV.
Week Four — Session Three
"""

import json
import csv

with open("students.json", "r") as f:
    data = json.load(f)

with open("students_export.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["ID", "Name", "Major"])
    for item in data:
        writer.writerow([item["id"], item["name"], item["major"]])

print("Exported JSON to CSV successfully!")
