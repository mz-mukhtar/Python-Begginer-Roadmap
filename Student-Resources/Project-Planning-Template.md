# 🛠️ Python Project Planning Template

Copy this reusable planning template into your project directory (as `PROJECT_PLAN.md`) before writing code. A well-planned software project is much easier to build, debug, and present!

---

## Student Information

```text
Student Name: 
Project Name: 
Course: Python Beginner to Practical Developer Roadmap
Start Date: 
Target Completion Date: 
```

---

## 1. Project Idea

> **What are you building?**
> *(Write a 2-3 sentence summary of your application idea.)*



---

## 2. Problem

> **What problem does the project solve?**
> *(Explain why this software is useful and what manual process it simplifies.)*



---

## 3. Target User

> **Who will use the project?**
> *(Describe the intended end user, such as a teacher, small business owner, student, or personal budgeter.)*



---

## 4. Main Features

| ID | Feature | Priority | Status |
| --- | --- | --- | --- |
| F-01 | Example: Interactive CLI Menu | Required | Complete |
| F-02 | | Required | Not Started |
| F-03 | | Required | Not Started |
| F-04 | | Important | Not Started |
| F-05 | | Optional | Not Started |

*(Priority Options: `Required`, `Important`, `Optional` | Status Options: `Not Started`, `In Progress`, `Complete`, `Needs Fixing`)*

---

## 5. Application Menu

Design your interactive numbered command menu:

```text
1. 
2. 
3. 
4. 
5. 
6. Exit
```

---

## 6. Data Requirements

| Data Field | Python Data Type | Required? | Example Value |
| --- | --- | --- | --- |
| `id` | String (`str`) | Yes | `"STU-001"` |
| | | | |
| | | | |

---

## 7. Functions

| Function Name | Responsibility | Input Parameters | Return Output |
| --- | --- | --- | --- |
| `display_menu()` | Prints the numbered CLI menu | None | None |
| | | | |
| | | | |

---

## 8. Classes

| Class Name | Responsibility | Attributes | Methods |
| --- | --- | --- | --- |
| | | | |
| | | | |

---

## 9. File Storage

Which file format will your application use for permanent data persistence?

```text
[ ] Text (.txt)
[ ] JSON (.json)
[ ] CSV (.csv)
[ ] Other: _________
```

---

## 10. Project Structure

Map out your project directory tree:

```text
project-name/
│
├── main.py
│
├── 
│
├── data/
│
└── README.md
```

---

## 11. External Packages

| Package Name | Purpose | Required for Project? |
| --- | --- | --- |
| | | |
| | | |

---

## 12. Error Handling Plan

Answer the following questions to make your application resilient against crashes:

- **What invalid input may happen?** *(e.g., user types text when a number is asked)*
  

- **What files may be missing on startup?** *(e.g., `data/records.json` does not exist yet)*
  

- **What Python exceptions should be caught and handled?** *(e.g., `ValueError`, `FileNotFoundError`, `JSONDecodeError`)*
  

---

## 13. Testing Plan

| Feature Tested | Test Input Given | Expected Result | Actual Result | Status |
| --- | --- | --- | --- | --- |
| Menu Exit | Option `6` | Program prints goodbye message and exits cleanly | | |
| | | | | |
| | | | | |

---

## 14. Git Plan

Check off your version control milestones as you work:

```text
[ ] Repository created (`git init`)
[ ] `.gitignore` added and verified
[ ] First commit created for project skeleton
[ ] Features committed separately with descriptive messages
[ ] Final version pushed to remote GitHub repository
```

---

## 15. Project Milestones

| Milestone | Target Date | Status |
| --- | --- | --- |
| Planning worksheet complete | | |
| Core menu and navigation working | | |
| CRUD operations implemented | | |
| File saving and loading working | | |
| Unit tests and documentation complete | | |

---

## 16. Challenges

> **What problems did you face during development?**



---

## 17. Solutions

> **How did you solve those problems?**



---

## 18. Future Improvements

> **If you had more time, what extra features would you add?**



---

## 19. Final Checklist

Verify your completed capstone project against course requirements:

```text
[ ] Application launches cleanly from the terminal without startup errors
[ ] Interactive numbered menu provides intuitive navigation
[ ] All user input is validated with crash-safe `try`/`except` blocks
[ ] Data is permanently saved to and loaded from disk (JSON/CSV)
[ ] Code is organized cleanly using functions or Object-Oriented classes
[ ] Project folder includes a thorough `README.md` with usage instructions
[ ] Automated unit tests verify core business logic
```
