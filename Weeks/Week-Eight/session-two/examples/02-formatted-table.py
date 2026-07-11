"""
Example: Displaying tabular data cleanly using string formatting.
Week Eight — Session Two
"""

records = [
    {"id": 101, "name": "Abel Tadesse", "age": 20, "major": "CS"},
    {"id": 102, "name": "Sara Kebede", "age": 19, "major": "EE"}
]

print(f"{'ID':<6} | {'NAME':<15} | {'AGE':<5} | {'MAJOR':<10}")
print("-" * 45)
for r in records:
    print(f"{r['id']:<6} | {r['name']:<15} | {r['age']:<5} | {r['major']:<10}")
