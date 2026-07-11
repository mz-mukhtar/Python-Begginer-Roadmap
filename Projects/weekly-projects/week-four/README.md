# Persistent Student Management System

## 📌 Project Description
The **Persistent Student Management System** connects our student records to the local file system. Using Python's `json` and `csv` standard modules alongside `pathlib`, records are automatically loaded from `data/students.json` on application startup, saved back to disk when modified, and exportable into spreadsheet-ready CSV files!

---

## 🎯 Learning Objectives
Students will practice:
- Reading and writing local files using `with open()`
- Serializing and deserializing lists of dictionaries to JSON files (`json.dump`/`json.load`)
- Checking file existence safely with `pathlib.Path`
- Exporting structured data to CSV files using `csv.writer`

---

## 🧠 Concepts Used
- **Weeks 1-3**: Variables, Loops, Lists, Dictionaries, Modular Functions.
- **Week 4**: Strings, Files, File Paths, `pathlib`, JSON, CSV.

---

## ✨ Features
- Automatic JSON data loading on startup (`data/students.json`)
- Full CRUD operations synced directly to permanent JSON storage
- Manual Save option (`6. Save Students`) and CSV Export option (`7. Export to CSV`)
- Safe directory creation using `pathlib`

---

## 📂 Project Structure
```text
week-four/
├── README.md
├── main.py
└── data/
    ├── students.json
    └── students.csv
```

---

## ▶️ How to Run
```bash
python main.py
```

---

## 🖥️ Example Output
```text
========================================
 PERSISTENT STUDENT MANAGEMENT (WEEK 4) 
========================================
Loaded 2 student records from disk.
1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Save Students
7. Export to CSV
8. Exit
========================================
Enter choice (1-8): 7
✅ Successfully exported 2 records to data/students.csv
```

---

## 🔍 How the Project Works
1. `load_students()` checks `Path("data/students.json").exists()`. If true, returns `json.load()`; otherwise returns `[]`.
2. Every modification can be saved using `save_students(roster)`.
3. `export_to_csv(roster)` opens `data/students.csv` and writes a header row followed by student rows.

---

## ✅ Project Checklist
- [x] Load student records from JSON on startup
- [x] Save updated records to JSON file
- [x] Export student records to CSV spreadsheet format
- [x] Use `pathlib` for file existence verification

---

## 🚀 Next Week
Next week, we add **Exception Handling (`try`/`except`) and Logging**, making our file storage completely crash-proof against corrupted files or invalid inputs!
