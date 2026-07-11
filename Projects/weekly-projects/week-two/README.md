# Student Information Collector

## 📌 Project Description
The **Student Information Collector** evolves our academic tool into a dynamic, multi-student command-line registry. Using interactive loops and Python collections, users can add multiple student records, view the entire classroom roster, search for individual students by name, and display a unique summary of all registered academic departments.

> **Educational Note**: During Week Three, this application will be reorganized using clean, modular functions. For Week Two, we write our procedural logic inside an interactive `while` loop!

---

## 🎯 Learning Objectives
Students will practice:
- Building interactive command-line menus using `while True` loops
- Storing multiple records inside Python `lists`
- Representing individual student records as structured `dictionaries`
- Extracting unique values across records using Python `sets`

---

## 🧠 Concepts Used
- **Week 1**: Variables, Input, Type Conversion, Conditions (`if`/`elif`/`else`).
- **Week 2**: `while` loops, `for` loops, `break`/`continue`, Lists, Tuples, Dictionaries, Sets.

---

## ✨ Features
- Menu-driven interface supporting repeated operations
- Add new students with Name, Age, Department, and Enrolled Courses list
- Display tabular list of all registered students
- Search for a student by full or partial name match
- View a deduplicated set of all unique departments on campus
- Clean application exit flow

---

## 📂 Project Structure
```text
week-two/
├── README.md
└── student_information_collector.py
```

---

## ▶️ How to Run
Execute in your terminal:
```bash
python student_information_collector.py
```

---

## 🖥️ Example Output
```text
========================================
     STUDENT INFORMATION COLLECTOR      
========================================
1. Add New Student
2. View All Students
3. Search Student by Name
4. View Unique Departments
5. Exit Application
========================================
Enter menu option (1-5): 1

--- Add New Student ---
Enter student name: Sara Ahmed
Enter student age: 20
Enter department: Computer Science
Enter enrolled courses (comma-separated): Python Basics, Calculus, Digital Logic
✅ Student Sara Ahmed added successfully!
```

---

## 🔍 How the Project Works
1. Maintains a main list `students_roster = []` to store records.
2. Inside a `while True` loop, displays numbered options `1` to `5`.
3. Option 1 collects inputs and appends a dictionary `{"name": name, "age": age, "department": dept, "courses": courses_list}`.
4. Option 2 loops through `students_roster` and prints formatted rows.
5. Option 3 searches records where search query matches student name case-insensitively.
6. Option 4 builds a Python `set` of departments to automatically eliminate duplicates.

---

## 🛠️ Student Improvement Ideas
- Add age range filtering (e.g., display all students aged 18 to 21).
- Calculate average age across the entire classroom roster.

---

## ✅ Project Checklist
- [x] Display interactive menu using a `while` loop
- [x] Add multiple students stored as dictionaries inside a list
- [x] Display all students cleanly
- [x] Search for a student by name
- [x] Use a set to display unique academic departments

---

## 🚀 Next Week
Next week, we will introduce **Modular Functions and Docstrings**, allowing us to organize this menu into clean, reusable functions!
