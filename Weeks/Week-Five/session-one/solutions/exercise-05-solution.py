"""
Exercise 5 Solution: Improve Previous Calculator
Week Five — Session One
"""

try:
    n1 = float(input("Num 1: "))
    n2 = float(input("Num 2: "))
    print("Division:", n1 / n2)
except (ValueError, ZeroDivisionError) as e:
    print("Calculation Error:", e)
