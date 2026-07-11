"""
Exercise 3 Solution: Prompt Positive Integer Safely
Week Eight — Session Two
"""

def get_int(prompt):
    while True:
        try: return int(input(prompt))
        except ValueError: print("Enter numeric digit.")
