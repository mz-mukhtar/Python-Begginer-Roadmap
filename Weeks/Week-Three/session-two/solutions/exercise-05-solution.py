"""
Exercise 5 Solution: Student Result Function
Week Three — Session Two
"""

def evaluate_score(score):
    """Returns Pass if score is 50 or above, otherwise Fail."""
    return "Pass" if score >= 50 else "Fail"

print(evaluate_score(75))
