"""
Challenge Solution: Student Information Collector
Week Two — Session Three
"""

student_list = []
unique_departments = set()

while True:
    name = input("Enter student name (or 'q' to stop): ").strip()
    if name.lower() == 'q':
        break
    age = int(input("Enter student age: "))
    dept = input("Enter student department: ").strip()

    student_list.append({"name": name, "age": age, "department": dept})
    unique_departments.add(dept)

print("")
print("=== ALL REGISTERED STUDENTS ===")
for s in student_list:
    print(f"Name: {s['name']} | Age: {s['age']} | Department: {s['department']}")

print("Unique Departments:", unique_departments)
