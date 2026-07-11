"""
Challenge Solution: Error-Safe Calculator
Week Five — Session One
"""

print("=== Error-Safe Calculator ===")
while True:
    op = input("Choose operation (+, -, *, /) or 'q' to quit: ").strip()
    if op == 'q':
        break
    if op not in ('+', '-', '*', '/'):
        print("Invalid operator.")
        continue
    try:
        a = float(input("First number: "))
        b = float(input("Second number: "))
        if op == '+': print("Result:", a + b)
        elif op == '-': print("Result:", a - b)
        elif op == '*': print("Result:", a * b)
        elif op == '/': print("Result:", a / b)
    except ValueError:
        print("Error: Please enter numeric values.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
