# Tested Student Management Capstone

## 📌 Project Description
The **Tested Student Management Capstone** represents the culmination of the 8-week Python roadmap. Integrating multi-file architecture, Object-Oriented models, file repository persistence, and comprehensive automated unit testing (`tests/`), this application verifies software reliability automatically!

---

## 🎯 Learning Objectives
Students will practice:
- Writing unit tests using Python's built-in `unittest` framework
- Testing domain models and controller services independently
- Executing automated test suites via `python -m unittest discover`

---

## 📂 Project Structure
```text
week-eight/
├── README.md
├── main.py
├── requirements.txt
├── .gitignore
├── models/
│   └── student.py
├── services/
│   └── student_manager.py
├── utilities/
│   └── file_manager.py
├── data/
│   └── students.json
└── tests/
    ├── __init__.py
    ├── test_student.py
    └── test_student_manager.py
```

---

## ▶️ How to Run Application
```bash
python main.py
```

## ▶️ How to Run Automated Unit Tests
```bash
python -m unittest discover tests
```

---

## ✅ Project Checklist
- [x] Complete multi-file package architecture
- [x] Automated unit test coverage for `Student` model
- [x] Automated unit test coverage for `StudentManager` controller

---

## 🚀 Next Learning Path
Congratulations on completing all 8 weekly projects! Explore the **`final-projects/`** directory to select and build your independent Capstone project!
