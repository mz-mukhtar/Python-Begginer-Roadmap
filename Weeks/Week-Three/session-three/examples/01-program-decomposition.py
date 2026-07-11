"""
Example: Breaking a program into input, processing, and output functions.
Week Three — Session Three
"""

def get_input():
    return 80, 90

def process(a, b):
    return a + b

def display(result):
    print("Total:", result)

a, b = get_input()
display(process(a, b))
