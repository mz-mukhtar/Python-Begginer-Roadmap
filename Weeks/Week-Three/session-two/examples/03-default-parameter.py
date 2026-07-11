"""
Example: Using default parameter values.
Week Three — Session Two
"""

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Abel"))
print(greet("Sara", "Welcome"))
