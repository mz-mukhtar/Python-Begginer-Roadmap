"""
Example: Returning a dictionary record from a creation function.
Week Three — Session Three
"""

def make_record(name, dept):
    return {"name": name, "department": dept}

print(make_record("Abel", "Engineering"))
