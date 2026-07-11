"""
Example: Writing structured records to a CSV file.
Week Four — Session Three
"""

import csv

records = [["ID", "Name"], ["1", "Abel"], ["2", "Sara"]]
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(records)
print("Wrote data.csv")
