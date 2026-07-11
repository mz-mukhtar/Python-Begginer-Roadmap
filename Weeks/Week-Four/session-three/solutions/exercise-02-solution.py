"""
Exercise 2 Solution: Load Products
Week Four — Session Three
"""

import json
with open("contacts.json", "r") as f:
    data = json.load(f)
print("Loaded:", data)
