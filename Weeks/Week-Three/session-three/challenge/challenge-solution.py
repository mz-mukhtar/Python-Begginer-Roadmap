"""
Challenge Solution: Function-Based Student Management System
Week Three — Session Three
"""

def add_student(roster, name, age):
    roster.append({"id": len(roster)+1, "name": name, "age": age})
    print(f"Added {name}")

def view_students(roster):
    for s in roster:
        print(f"ID: {s['id']} | Name: {s['name']} | Age: {s['age']}")

def delete_student(roster, target_id):
    for i, s in enumerate(roster):
        if s["id"] == target_id:
            removed = roster.pop(i)
            print(f"Deleted {removed['name']}")
            return
    print("Student ID not found.")

roster = []
add_student(roster, "Abel", 20)
add_student(roster, "Sara", 19)
view_students(roster)
delete_student(roster, 1)
view_students(roster)
