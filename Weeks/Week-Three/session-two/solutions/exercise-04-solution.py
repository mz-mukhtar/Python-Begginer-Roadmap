"""
Exercise 4 Solution: Default Greeting
Week Three — Session Two
"""

def greet(name, lang="English"):
    if lang == "Amharic":
        return f"Selam, {name}!"
    return f"Hello, {name}!"

print(greet("Abel", "Amharic"))
