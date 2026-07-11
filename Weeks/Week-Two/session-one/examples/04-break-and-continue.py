"""
Example: Using break to stop loop and continue to skip step.
Week Two — Session One
"""

print("=== Continue Example (Skip 3) ===")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

print("=== Break Example (Stop at 4) ===")
for i in range(1, 6):
    if i == 4:
        break
    print(i)
