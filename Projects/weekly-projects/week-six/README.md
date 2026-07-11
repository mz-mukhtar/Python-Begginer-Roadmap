# Object-Oriented Student Management System

## 📌 Project Description
The **Object-Oriented Student Management System** replaces plain dictionaries with formal Object-Oriented blueprints. By defining a parent class `User`, a child class `Student(User)`, and a coordinating controller class `StudentManager`, students experience encapsulation, basic inheritance, and clean serialization (`to_dict` / `from_dict`) in action.

---

## 🎯 Learning Objectives
Students will practice:
- Creating Python classes with constructors (`__init__`)
- Implementing inheritance hierarchy (`User` -> `Student`)
- Coordinating collections of objects using a Manager class (`StudentManager`)
- Converting object instances into JSON-serializable dictionaries

---

## 🧠 Concepts Used
- **Weeks 1-5**: All fundamental Python flow, JSON persistence, and error handling.
- **Week 6**: Classes, Objects, Methods, Constructors, Basic Inheritance.

---

## ✨ Features
- `User` parent class encapsulating common attributes
- `Student` child class extending attributes with academic major and GPA
- `StudentManager` coordinating all CRUD and JSON persistence operations
- Clean single-file educational layout

---

## 📂 Project Structure
```text
week-six/
├── README.md
├── main.py
└── data/
    └── students.json
```

---

## ▶️ How to Run
```bash
python main.py
```

---

## ✅ Project Checklist
- [x] Create `User` base class and `Student` child class
- [x] Implement `to_dict()` and `from_dict()` serialization
- [x] Build `StudentManager` class coordinating operations

---

## 🚀 Next Week
Next week, we divide our Object-Oriented classes into a **Professionally Organized Multi-File Architecture (`models/`, `services/`, `utilities/`)**!
