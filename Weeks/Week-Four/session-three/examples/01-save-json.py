"""
Example: Saving Python lists/dicts to a JSON file.
Week Four — Session Three
"""

import json

data = [{"name": "Abel", "score": 90}]
with open("scores.json", "w") as f:
    json.dump(data, f, indent=4)
print("Saved scores.json")
