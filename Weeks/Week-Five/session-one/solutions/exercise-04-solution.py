"""
Exercise 4 Solution: Score Validation
Week Five — Session One
"""

while True:
    try:
        s = float(input("Score (0-100): "))
        if 0 <= s <= 100:
            print("Valid score:", s)
            break
        print("Out of range.")
    except ValueError:
        print("Must be numeric.")
