"""
Exercise 3 Solution: Calculate Discount
Week Three — Session Two
"""

def calculate_discount(price, rate=0.10):
    return price * (1 - rate)

print("Discounted:", calculate_discount(100))
