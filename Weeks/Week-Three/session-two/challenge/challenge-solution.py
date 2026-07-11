"""
Challenge Solution: Reusable Grade Calculator
Week Three — Session Two
"""

def calculate_student_summary(name, scores):
    """Calculates summary metrics and returns a structured dictionary."""
    total = sum(scores)
    avg = total / len(scores)
    if avg >= 85:
        grade = "A"
    elif avg >= 70:
        grade = "B"
    elif avg >= 50:
        grade = "C"
    else:
        grade = "F"

    return {
        "name": name,
        "total": total,
        "average": round(avg, 2),
        "grade": grade
    }

summary = calculate_student_summary("Mahi", [90, 88, 94])
print("Student Summary:", summary)
