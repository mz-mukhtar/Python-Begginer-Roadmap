"""
Exercise 6 Solution: Discount Calculator
Week One — Session Three
"""

purchase = float(input("Enter purchase amount: "))
if purchase >= 1000:
    discount = 0.20
elif purchase >= 500:
    discount = 0.10
else:
    discount = 0.0

final_price = purchase * (1 - discount)
print("Final Price:", final_price)
