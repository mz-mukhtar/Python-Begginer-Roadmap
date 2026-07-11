"""
Example: Passing keyword arguments.
Week Three — Session Two
"""

def create_profile(name, age, city):
    return f"{name} ({age}) from {city}"

profile = create_profile(age=20, city="Addis Ababa", name="Abel")
print(profile)
