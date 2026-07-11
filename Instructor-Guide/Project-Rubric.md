# 🏆 Final Project Evaluation Rubric

Use this transparent, 100-point evaluation rubric to grade student capstone final projects (`Projects/final-projects/`) and live technical presentations.

---

## Recommended Scoring Summary

| Evaluation Category | Allocated Points |
| --- | :---: |
| **Project Planning** | 5 |
| **Program Functionality** | 20 |
| **Required Features** | 15 |
| **Python Fundamentals** | 10 |
| **Functions and Organization** | 10 |
| **File Storage** | 5 |
| **Error Handling** | 5 |
| **Object-Oriented Programming** | 10 |
| **Testing** | 5 |
| **Code Readability** | 5 |
| **Documentation** | 5 |
| **Git Usage** | 2 |
| **Presentation** | 3 |
| **Total Score** | **100** |

---

## Detailed Evaluation Criteria

### 1. Project Planning (5 Points)
- **Excellent (5 pts)**: Complete, detailed `PROJECT_PLAN.md` worksheet showing clear target users, feature priorities, menu design, and test cases.
- **Good (4 pts)**: Planning worksheet complete with minor missing details.
- **Developing (2–3 pts)**: Partial planning worksheet submitted with several incomplete sections.
- **Needs Improvement (0–1 pts)**: No formal planning worksheet submitted.

### 2. Program Functionality (20 Points)
- **Excellent (18–20 pts)**: Application starts reliably from terminal, numbered CLI menu navigates smoothly, all options work without crashes, exits cleanly.
- **Good (15–17 pts)**: Application runs reliably; most features work with minor visual or navigation quirks.
- **Developing (10–14 pts)**: Application runs but crashes on certain menu options or edge cases.
- **Needs Improvement (0–9 pts)**: Application fails to run due to syntax errors or startup crashes.

### 3. Required Features (15 Points)
- **Excellent (14–15 pts)**: Implements all required domain features (CRUD workflows, filtering, searching, exporting).
- **Good (11–13 pts)**: Implements core CRUD features with one secondary option incomplete.
- **Developing (7–10 pts)**: Implements partial CRUD functionality (e.g., can Add and View but cannot Update or Delete).
- **Needs Improvement (0–6 pts)**: Missing most required core business features.

### 4. Python Fundamentals (10 Points)
- **Excellent (9–10 pts)**: Demonstrates clean mastery of typed variables, conditional branching (`if`/`elif`/`else`), loops (`while`/`for`), and collections (`list`, `dict`).
- **Good (7–8 pts)**: Solid use of core syntax with minor redundant loops or conditions.
- **Developing (4–6 pts)**: Basic syntax used correctly but struggles with data collection manipulation.
- **Needs Improvement (0–3 pts)**: Substantial syntax errors or incorrect operator usage.

### 5. Functions and Organization (10 Points)
- **Excellent (9–10 pts)**: Code is decomposed into single-responsibility functions with clear parameters, return values, docstrings, and a coordinating `main()`.
- **Good (7–8 pts)**: Functions used effectively; minor duplication or over-extended function blocks.
- **Developing (4–6 pts)**: Program relies heavily on procedural script flow with minimal function reuse.
- **Needs Improvement (0–3 pts)**: All application logic written inside a single unstructured block.

### 6. File Storage (5 Points)
- **Excellent (5 pts)**: Data saves automatically to JSON/CSV files and reloads cleanly on startup using `pathlib` and context managers (`with open()`).
- **Good (4 pts)**: File saving/loading works correctly with minor edge case issues on missing files.
- **Developing (2–3 pts)**: Can write to files but struggles to reload data back into memory.
- **Needs Improvement (0–1 pts)**: No permanent file storage implemented (data lost on exit).

### 7. Error Handling (5 Points)
- **Excellent (5 pts)**: Uses targeted `try`/`except` blocks (`ValueError`, `FileNotFoundError`, `JSONDecodeError`) to prevent crashes on invalid user input.
- **Good (4 pts)**: Good input validation; handles numeric errors well.
- **Developing (2–3 pts)**: Uses generic `except:` blocks or misses common numeric input crashes.
- **Needs Improvement (0–1 pts)**: No error handling implemented; invalid input crashes the program immediately.

### 8. Object-Oriented Programming (10 Points)
- **Excellent (9–10 pts)**: Defines clean domain classes (`__init__`, `self`, instance methods) and controller classes with clear separation of responsibilities.
- **Good (7–8 pts)**: Classes used correctly; minor mixing of CLI print statements inside domain models.
- **Developing (4–6 pts)**: Classes defined but treated simply as passive data dictionaries without instance methods.
- **Needs Improvement (0–3 pts)**: OOP concepts omitted or implemented incorrectly.

### 9. Testing (5 Points)
- **Excellent (5 pts)**: Includes an automated unit test suite (`unittest.TestCase`) verifying domain models and CRUD services; runs cleanly with `OK`.
- **Good (4 pts)**: Includes working unit tests covering at least two core functions.
- **Developing (2–3 pts)**: Basic test file present but tests are incomplete or failing.
- **Needs Improvement (0–1 pts)**: No automated tests submitted.

### 10. Code Readability (5 Points)
- **Excellent (5 pts)**: Descriptive variable/function names, clean 4-space indentation, clear inline comments, and docstrings throughout.
- **Good (4 pts)**: Readable code with minor naming or formatting inconsistencies.
- **Developing (2–3 pts)**: Vague variable names (`x`, `data1`) or inconsistent formatting.
- **Needs Improvement (0–1 pts)**: Messy, unindented, or unreadable code.

### 11. Documentation (5 Points)
- **Excellent (5 pts)**: Professional project `README.md` containing features, folder tree, run commands, example output, and developer notes.
- **Good (4 pts)**: Complete `README.md` with minor missing usage details.
- **Developing (2–3 pts)**: Brief 5-line `README.md` submitted.
- **Needs Improvement (0–1 pts)**: No project documentation provided.

### 12. Git Usage (2 Points)
- **Excellent (2 pts)**: Clean Git commit history with descriptive messages and a proper `.gitignore` file excluding `.venv/` and `__pycache__/`.
- **Good (1.5 pts)**: Working Git repository; commit messages slightly vague.
- **Developing (1 pt)**: Single monolithic commit at the very end of the project.
- **Needs Improvement (0 pts)**: No Git version control used.

### 13. Presentation (3 Points)
- **Excellent (3 pts)**: Concise, professional live demonstration clearly explaining problem, features, and code architecture.
- **Good (2 pts)**: Good demonstration; slightly rushed or hesitant during code explanation.
- **Developing (1 pt)**: Demonstrates application running but struggles to explain code architecture.
- **Needs Improvement (0 pts)**: No presentation delivered.

---

## Required Feature Checklist

Verify that the student's capstone project implements the standard core developer checklist:

```text
[ ] Add new records safely via CLI prompts
[ ] View and list existing records with clean formatting
[ ] Search for specific records by ID, name, or keyword
[ ] Update existing record attributes
[ ] Delete records with confirmation prompt
[ ] Save data permanently to local disk (JSON/CSV)
[ ] Load existing data automatically on startup
[ ] Validate user input using crash-safe `try`/`except` blocks
[ ] Handle missing or corrupted files gracefully
[ ] Encapsulate data inside Object-Oriented classes
[ ] Verify business logic using automated unit tests
[ ] Include a comprehensive project README.md
```

---

## Project Presentation Rubric (3 Points Total)

| Presentation Area | Points | Criteria |
| --- | :---: | --- |
| **Problem Explanation** | 1 | Clearly articulates what problem the software solves and who will use it |
| **Feature Demonstration** | 1 | Live-demos interactive CLI menu navigation and permanent file storage |
| **Code Explanation** | 1 | Confidently explains how classes, functions, and file handlers interact |

---

## Instructor Comment Section

```text
Strengths:
_______________________________________________________________________________

Areas for Improvement:
_______________________________________________________________________________

Recommended Next Steps:
_______________________________________________________________________________

Final Score: ________ / 100

Instructor Name: ___________________________        Date: ____________________
```

---

## Bonus Recognition Awards

Instructors may award these non-graded recognition distinctions during capstone showcase graduation:
- 🌟 **Best Technical Implementation**: Awarded for outstanding architecture, unit testing, and error resilience.
- 🎨 **Best User Experience**: Awarded for the most intuitive, cleanly formatted CLI menu navigation.
- 📚 **Best Documentation**: Awarded for the most thorough, professional project `README.md`.
- 💡 **Most Creative Project**: Awarded for an innovative application idea solving a unique problem.
- 🚀 **Most Improved Student**: Awarded to a learner who demonstrated exceptional dedication and growth across the 8 weeks.
