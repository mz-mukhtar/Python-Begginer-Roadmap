"""
Example: Checking if score is within valid 0-100 range.
Week One — Session Three
"""

score = 105

if score < 0 or score > 100:
    print("Error: Invalid score entered!")
else:
    print("Valid score:", score)
