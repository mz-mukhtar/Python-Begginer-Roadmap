# Reliable Student Management System

## 📌 Project Description
The **Reliable Student Management System** introduces industrial-grade resilience to our persistent application. Using Python's `try`/`except` exception blocks, modular helper packages (`student_tools.py`), and standard `logging` (`logger_config.py`), the program logs important workflow milestones and gracefully recovers from corrupted JSON files or invalid user inputs!

---

## 🎯 Learning Objectives
Students will practice:
- Writing crash-proof input loops using `try`/`except ValueError`
- Handling file system exceptions (`FileNotFoundError`, `JSONDecodeError`)
- Dividing logic across custom helper modules (`student_tools.py`)
- Tracking application workflow using standard Python `logging`

---

## 🧠 Concepts Used
- **Weeks 1-4**: Functions, File I/O, JSON, CSV.
- **Week 5**: `try`/`except`/`else`/`finally`, Custom Modules, Standard `logging`.

---

## ✨ Features
- Automatic log activity recording to `logs/system.log`
- Resilient JSON loader that recovers gracefully if `students.json` is corrupted
- Safe numeric input prompts preventing program crashes
- Modular separation between CLI controller (`main.py`) and data tools (`student_tools.py`)

---

## 📂 Project Structure
```text
week-five/
├── README.md
├── main.py
├── student_tools.py
├── logger_config.py
├── data/
│   └── students.json
└── logs/
    └── .gitkeep
```

---

## ▶️ How to Run
```bash
python main.py
```

---

## ✅ Project Checklist
- [x] Use `try`/`except` for numeric inputs and JSON loading
- [x] Separate helper functions into `student_tools.py`
- [x] Log application start, CRUD actions, and errors to `logs/system.log`

---

## 🚀 Next Week
Next week, we refactor our data dictionaries into **Object-Oriented Classes (`Student`, `User`, `StudentManager`)**!
