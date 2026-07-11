"""
Example: Robust input validation loop.
Week Five — Session One
"""

def get_positive_age():
    while True:
        try:
            val = int(input("Enter your age: "))
            if val > 0:
                return val
            print("Age must be positive.")
        except ValueError:
            print("Invalid input. Enter a whole number.")
