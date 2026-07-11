"""
Example: Using try, except, else, and finally.
Week Five — Session One
"""

try:
    number = int("50")
except ValueError:
    print("Conversion failed.")
else:
    print("Conversion successful! Number is:", number)
finally:
    print("Execution check complete.")
