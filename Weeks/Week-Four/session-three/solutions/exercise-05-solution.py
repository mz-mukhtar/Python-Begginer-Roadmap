"""
Exercise 5 Solution: Export JSON Data to CSV
Week Four — Session Three
"""

import json, csv
with open("contacts.json", "r") as f:
    data = json.load(f)
with open("contacts.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["Name", "Phone"])
    for d in data:
        w.writerow([d["name"], d["phone"]])
print("Exported.")
