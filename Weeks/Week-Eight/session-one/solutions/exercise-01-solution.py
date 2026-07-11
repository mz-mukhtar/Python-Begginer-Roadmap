"""
Exercise 1 Solution: Save Roster to JSON
Week Eight — Session One
"""

import json
def save_roster(file, data):
    with open(file, "w") as f: json.dump(data, f, indent=4)
print("Save roster implemented.")
