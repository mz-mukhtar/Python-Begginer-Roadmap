# Professionally Organized Student Management System

## 📌 Project Description
The **Professionally Organized Student Management System** transitions our OOP code into an industry-standard multi-file project architecture. Domain models reside inside `models/`, business controllers inside `services/`, and storage utilities inside `utilities/`, all coordinated cleanly by `main.py`.

---

## 🎯 Learning Objectives
Students will practice:
- Structuring multi-file Python packages (`models`, `services`, `utilities`)
- Using `__init__.py` package initializers and modular imports
- Configuring project dependencies (`requirements.txt`) and `.gitignore`

---

## 📂 Project Structure
```text
week-seven/
├── README.md
├── main.py
├── requirements.txt
├── .gitignore
├── models/
│   ├── __init__.py
│   └── student.py
├── services/
│   ├── __init__.py
│   └── student_manager.py
├── utilities/
│   ├── __init__.py
│   └── file_manager.py
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
- [x] Separate code into `models`, `services`, and `utilities` modules
- [x] Configure standard `.gitignore` and `requirements.txt`
- [x] Coordinate cleanly from `main.py` entrypoint

---

## 🚀 Next Week
Next week, we add automated **Unit Tests (`unittest`)** to create our verified capstone!
