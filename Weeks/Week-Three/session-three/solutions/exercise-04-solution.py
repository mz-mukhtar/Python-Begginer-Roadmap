"""
Exercise 4 Solution: Create Search Function
Week Three — Session Three
"""

def search_student(roster, name):
    for s in roster:
        if s["name"].lower() == name.lower():
            return s
    return None

roster = [{"name": "Abel", "age": 20}]
print("Found:", search_student(roster, "abel"))
