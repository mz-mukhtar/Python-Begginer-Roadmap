"""
Custom module with helper math functions.
Week Five — Session Two
"""

def add_scores(scores):
    return sum(scores)

def average_score(scores):
    return sum(scores) / len(scores) if scores else 0
