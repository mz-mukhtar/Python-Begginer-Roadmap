"""
Example: Resilient CLI input prompt helper.
Week Eight — Session Two
"""

def prompt_int(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Please enter a valid number.")
