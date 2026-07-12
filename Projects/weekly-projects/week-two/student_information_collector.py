"""
Project: Student Information Collector
Week Two — Python Beginner Roadmap
Author: Mahi Zeki (EthioNext / Harar Dev Center / Cyber Vanguard)

Description:
An interactive student registry utilizing loops, lists, dictionaries, and sets.
Note: Custom functions are intentionally avoided until Week Three.
"""

# Main classroom roster list to store student dictionary records
students_roster = []

print("Welcome to the Student Information Collector v2.0!")

while True:
    print("")
    print("========================================")
    print("     STUDENT INFORMATION COLLECTOR      ")
    print("========================================")
    print("1. Add New Student")
    print("2. View All Students")
    print("3. Search Student by Name")
    print("4. View Unique Departments")
    print("5. Exit Application")
    print("========================================")

    choice = input("Enter menu option (1-5): ").strip()

    if choice == "1":
        print("")
        print("--- Add New Student ---")
        name = input("Enter student name: ").strip()
        age_str = input("Enter student age: ").strip()
        department = input("Enter department: ").strip()
        courses_raw = input("Enter enrolled courses (comma-separated): ").strip()

        # Convert numeric age safely
        if age_str.isdigit():
            age = int(age_str)
        else:
            age = 18  # Default fallback if non-numeric

        # Convert comma-separated courses into a list of cleaned strings
        courses_list = []
        for c in courses_raw.split(","):
            cleaned = c.strip()
            if cleaned:
                courses_list.append(cleaned)

        # Build student dictionary and append to main list
        student_record = {
            "name": name,
            "age": age,
            "department": department,
            "courses": courses_list
        }
        students_roster.append(student_record)
        print(f"✅ Student {name} added successfully!")

    elif choice == "2":
        print("")
        print("--- All Registered Students ---")
        if not students_roster:
            print("No students registered yet.")
        else:
            for idx, student in enumerate(students_roster, 1):
                print(f"{idx}. {student['name']} | Age: {student['age']} | Dept: {student['department']}")
                print(f"   Courses: {', '.join(student['courses'])}")

    elif choice == "3":
        print("")
        search_query = input("Enter student name to search: ").strip().lower()
        found = False
        for student in students_roster:
            if search_query in student["name"].lower():
                print(f"🎯 MATCH: {student['name']} ({student['age']}) - Dept: {student['department']}")
                found = True
        if not found:
            print("No matching student found.")

    elif choice == "4":
        print("")
        print("--- Unique Academic Departments ---")
        departments_set = set()
        for student in students_roster:
            departments_set.add(student["department"])

        if not departments_set:
            print("No departments registered.")
        else:
            for dept in sorted(departments_set):
                print(f"• {dept}")

    elif choice == "5":
        print("")
        print("Thank you for using Student Information Collector. Goodbye!")
        break

    else:
        print("❌ Invalid selection. Please choose an option between 1 and 5.")
