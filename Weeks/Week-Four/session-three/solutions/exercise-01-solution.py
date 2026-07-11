"""
Exercise 1 Solution: Save Contact Information
Week Four — Session Three
"""

import json
contacts = [{"name": "Abel", "phone": "0911000000"}]
with open("contacts.json", "w") as f:
    json.dump(contacts, f, indent=4)
print("Contacts saved.")
