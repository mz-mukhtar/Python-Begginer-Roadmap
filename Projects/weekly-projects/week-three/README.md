# Function-Based Student Management System

## 📌 Project Description
The **Function-Based Student Management System** reorganizes our student application into a professional, modular architecture using single-responsibility Python functions. Learners implement full CRUD (Create, Read, Update, Delete) capabilities with clean parameter passing, return values, and structured docstrings.

> **Limitation Note**: Data is currently stored in-memory during execution. When the program closes, records are reset. Next week (Week Four), we will introduce JSON and CSV persistence so records are saved permanently!

---

## 🎯 Learning Objectives
Students will practice:
- Decomposing monolithic programs into focused, single-purpose functions
- Passing lists and dictionary records as function arguments
- Returning status flags and lookup records from functions
- Documenting functions with clear Python docstrings

---

## 🧠 Concepts Used
- **Weeks 1-2**: Variables, Conditions, Loops, Lists, Dictionaries.
- **Week 3**: Function definitions (`def`), Parameters, Return values, Scope, Default arguments, Docstrings.

---

## ✨ Features
- Clean CLI menu loop coordinated by a `main()` controller function
- Add new student records with unique Student IDs
- View formatted table of all registered students
- Search for specific students by ID or Name
- Update existing student major or age
- Delete student records cleanly by ID

---

## 📂 Project Structure
```text
week-three/
├── README.md
└── student_management_system.py
```

---

## ▶️ How to Run
```bash
python student_management_system.py
```

---

## 🖥️ Example Output
```text
========================================
   STUDENT MANAGEMENT SYSTEM (WEEK 3)   
========================================
1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
========================================
Enter choice (1-6): 1
Enter Student ID: STU-101
Enter Student Name: Sara Ahmed
Enter Age: 20
Enter Department: Computer Science
✅ Student Sara Ahmed added successfully.
```

---

## 🔍 How the Project Works
1. `display_menu()` renders numbered options `1` to `6`.
2. `create_student(sid, name, age, department)` returns a clean dictionary record.
3. `add_student(roster, student)` validates duplicate IDs and appends to the roster list.
4. `search_student(roster, sid)` returns the matching student record or `None`.
5. `update_student()` and `delete_student()` modify or remove records in place.
6. `main()` coordinates the interactive execution loop.

---

## 🛠️ Student Improvement Ideas
- Add confirmation prompts before deleting a student record.
- Support sorting student list alphabetically by name.

---

## ✅ Project Checklist
- [x] Implement all required functions (`display_menu`, `create_student`, `add_student`, `view_students`, `search_student`, `update_student`, `delete_student`, `main`)
- [x] Use clean parameter passing and return values
- [x] Document every function with a clear docstring
- [x] Provide full CRUD capabilities

---

## 🚀 Next Week
Next week, we add **Data Persistence (JSON and CSV files)** so your student records stay saved on disk even after restarting the computer!
