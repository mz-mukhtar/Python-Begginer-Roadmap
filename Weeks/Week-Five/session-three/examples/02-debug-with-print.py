"""
Example: Print debugging technique.
Week Five — Session Three
"""

def compute_total(items):
    total = 0
    for i in items:
        # print("DEBUG - current item:", i, "subtotal before:", total)
        total += i
    return total

print("Total:", compute_total([10, 20, 30]))
