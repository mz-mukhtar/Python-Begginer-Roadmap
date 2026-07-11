"""
Example: Consistent success and error status messages.
Week Eight — Session Two
"""

def print_success(msg):
    print("✅ SUCCESS:", msg)

def print_error(msg):
    print("❌ ERROR:", msg)

print_success("Student added successfully.")
print_error("Student ID already exists.")
