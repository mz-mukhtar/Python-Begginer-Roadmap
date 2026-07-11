# 📘 Instructor Session Delivery Plans

This guide contains structured, actionable lesson delivery plans for all 24 sessions across the 8-week curriculum. Use these plans to guide classroom pacing, live demonstrations, guided activities, and formative assessments.

---

## Week One — Python Foundations

### Week 1, Session 1: Introduction to Python
- **Week**: 1
- **Session**: 1
- **Topic**: Introduction to Python & Programming Setup
- **Duration**: 3 Hours
- **Main Goal**: Students should install Python, configure VS Code, and execute their first Python script from the terminal.
- **Required Preparation**: Verify Python 3 installation packages and VS Code setup on classroom computers.
- **Learning Objectives**: Students can explain what Python is, create a `.py` script, and use `print()` to output text.
- **Topics**: Programming concepts, Python uses, IDE installation, syntax rules, indentation, comments, `print()`.
- **Demonstration**: Live code `print("Hello, Python!")` and execute it in terminal. Show how syntax errors happen when quotes are missing.
- **Guided Activity**: Students write `examples/01-hello_world.py` and run it locally.
- **Independent Activity**: Students create a personal introduction script printing name, hobby, and goals.
- **Assessment**: Verify each student runs their script without terminal errors.
- **Homework**: Read Week 1 Session 2 preview and practice printing ASCII art.
- **Common Problems**: `python` command not found; saving `.txt` instead of `.py`.
- **Teaching Notes**: Do not move forward until 100% of students can successfully execute a script from their terminal.

### Week 1, Session 2: Variables, Data Types, Input, and Operators
- **Week**: 1
- **Session**: 2
- **Topic**: Variables, Data Types, Input, and Operators
- **Duration**: 3 Hours
- **Main Goal**: Students should capture keyboard input, store values in typed variables, and perform arithmetic calculations.
- **Required Preparation**: Prepare diagrams illustrating variable memory boxes and type casting (`int()`, `float()`).
- **Learning Objectives**: Students can use `input()`, convert string input to numbers, and apply arithmetic/comparison operators.
- **Topics**: Variables, strings, integers, floats, booleans, `type()`, `input()`, casting, operators (`+`, `-`, `*`, `/`).
- **Demonstration**: Live code an interactive age doubling script showing why `input()` requires `int()` casting before math.
- **Guided Activity**: Complete the interactive Simple Calculator exercise (`exercises/starter/`).
- **Independent Activity**: Build a bill splitter calculator that calculates tip and splits totals across people.
- **Assessment**: Ask students to explain what data type `input()` returns by default (`str`).
- **Homework**: Complete any unfinished Week 1 Session 2 practice exercises.
- **Common Problems**: `TypeError` when adding strings and integers together.
- **Teaching Notes**: Emphasize that variable names should be descriptive (`student_age` rather than `x`).

### Week 1, Session 3: Conditions and Weekly Project
- **Week**: 1
- **Session**: 3
- **Topic**: Conditional Branching (`if`/`elif`/`else`) & Weekly Project
- **Duration**: 3 Hours
- **Main Goal**: Students should build conditional branching logic and complete the Smart Student Grade System project.
- **Required Preparation**: Review comparison operators (`>=`, `<=`) and logical operators (`and`, `or`, `not`).
- **Learning Objectives**: Students can branch program flow using `if`/`elif`/`else` and evaluate multi-condition rules.
- **Topics**: Conditional branches, logical operators, nested conditions, boundary checks, weekly project development.
- **Demonstration**: Live code a pass/fail evaluator that checks if a score is between `0` and `100`.
- **Guided Activity**: Walk through the Smart Student Grade System requirement specification.
- **Independent Activity**: Students build and test `Projects/weekly-projects/week-one/student_grade_system.py`.
- **Assessment**: Grade weekly project against the 100-point rubric (focus on conditional logic accuracy).
- **Homework**: Complete Week 1 Learning Checklist and quiz.
- **Common Problems**: Using `=` (assignment) instead of `==` (comparison) inside `if` statements.
- **Teaching Notes**: Remind students to test edge cases (`0`, `100`, and invalid negative numbers).

---

## Week Two — Loops and Python Collections

### Week 2, Session 1: `while` and `for` Loops
- **Week**: 2
- **Session**: 1
- **Topic**: Iteration with `while` and `for` Loops
- **Duration**: 3 Hours
- **Main Goal**: Students should write loops to repeat actions and iterate over numeric ranges.
- **Required Preparation**: Prepare loop tracing diagrams showing counter increments and exit conditions.
- **Learning Objectives**: Students can write `while` loops, use `range()` with `for` loops, and control flow with `break`/`continue`.
- **Topics**: `while` loops, `for` loops, `range()`, loop counters, infinite loops, `break`, `continue`.
- **Demonstration**: Live code an interactive menu loop that repeats until the user enters option `'6'`.
- **Guided Activity**: Complete the Number Guessing Game loop exercise.
- **Independent Activity**: Build a multiplication table generator for numbers 1 to 10.
- **Assessment**: Check student code to ensure `while` loops increment counter variables correctly.
- **Homework**: Practice loop exercises from Session 1 folder.
- **Common Problems**: Infinite loops caused by forgetting `count += 1`.
- **Teaching Notes**: Show students how to press `Ctrl+C` in the terminal to kill an accidental infinite loop.

### Week 2, Session 2: Lists and Tuples
- **Week**: 2
- **Session**: 2
- **Topic**: Lists and Tuples
- **Duration**: 3 Hours
- **Main Goal**: Students should store, index, slice, and modify collections of data using Python lists.
- **Required Preparation**: Prepare visual index cards showing 0-indexed positions (`0, 1, 2`) and negative indexes (`-1`).
- **Learning Objectives**: Students can create lists, add/remove items, slice subsets, and differentiate lists from tuples.
- **Topics**: Creating lists, indexing, slicing, methods (`append`, `remove`, `pop`, `sort`), tuples vs. lists.
- **Demonstration**: Live code a classroom roster list that adds new students and prints the total count.
- **Guided Activity**: Complete the Dynamic Classroom Roster exercise.
- **Independent Activity**: Build a shopping list manager that lets users add, remove, and sort items.
- **Assessment**: Ask students why accessing index `3` on a 3-item list raises `IndexError`.
- **Homework**: Review dictionary syntax preview for Session 3.
- **Common Problems**: `IndexError: list index out of range` due to 1-based index assumptions.
- **Teaching Notes**: Clarify that tuples use parentheses `()` and cannot be changed after creation.

### Week 2, Session 3: Dictionaries, Sets, and Weekly Project
- **Week**: 2
- **Session**: 3
- **Topic**: Dictionaries, Sets & Student Information Collector Project
- **Duration**: 3 Hours
- **Main Goal**: Students should structure records using dictionaries and build the Week 2 weekly project.
- **Required Preparation**: Review key-value pairs and unique set collections.
- **Learning Objectives**: Students can create dictionaries, retrieve values safely with `.get()`, and use sets to deduplicate data.
- **Topics**: Dictionaries, key-value lookup, dictionary methods, nested records, sets, unique values, weekly project.
- **Demonstration**: Live code a dictionary storing a student's name, age, and major, then add it to a roster list.
- **Guided Activity**: Walk through the Student Information Collector specification.
- **Independent Activity**: Students build `Projects/weekly-projects/week-two/student_information_collector.py`.
- **Assessment**: Verify weekly project stores records inside dictionaries and deduplicates campus departments using a set.
- **Homework**: Complete Week 2 Learning Checklist and quiz.
- **Common Problems**: `KeyError` when looking up a missing dictionary key directly with square brackets.
- **Teaching Notes**: Encourage students to use `.get("key", default)` to prevent dictionary lookup crashes.

---

## Week Three — Functions and Program Organization

### Week 3, Session 1: Function Fundamentals
- **Week**: 3
- **Session**: 1
- **Topic**: Defining and Calling Functions (`def`)
- **Duration**: 3 Hours
- **Main Goal**: Students should write reusable custom functions that accept positional parameters.
- **Required Preparation**: Prepare code examples showing why copy-pasted code is hard to maintain.
- **Learning Objectives**: Students can define functions with `def`, pass arguments, and invoke functions from main code.
- **Topics**: What functions are, code reuse, defining functions, calling functions, parameters, arguments.
- **Demonstration**: Live code a `greet_student(name, course)` function and call it three times with different arguments.
- **Guided Activity**: Complete function definition exercises in `exercises/starter/`.
- **Independent Activity**: Write a utility function that formats a student ID and prints a welcome badge.
- **Assessment**: Check that students call functions with matching argument counts.
- **Homework**: Practice defining simple math functions.
- **Common Problems**: Defining a function but forgetting to call it (`greet_student("Sara")`).
- **Teaching Notes**: Emphasize that functions do nothing until explicitly invoked.

### Week 3, Session 2: Return Values and Scope
- **Week**: 3
- **Session**: 2
- **Topic**: Return Values, Default Parameters, and Variable Scope
- **Duration**: 3 Hours
- **Main Goal**: Students should write functions that return calculated data back to callers.
- **Required Preparation**: Prepare diagrams illustrating local function memory scope vs. global script scope.
- **Learning Objectives**: Students can use `return`, explain local scope, and set default parameter values.
- **Topics**: `return` statements, local vs. global scope, default parameters, keyword arguments, docstrings.
- **Demonstration**: Live code `calculate_average(scores)` that returns a float value to be stored in a variable.
- **Guided Activity**: Build a modular calculation script that returns grades and honors status.
- **Independent Activity**: Create a financial discount calculator function with a default discount rate of `10%`.
- **Assessment**: Ask students why a variable defined inside a function cannot be printed outside that function.
- **Homework**: Review function decomposition principles for Session 3.
- **Common Problems**: Confusing `print(x)` inside a function with `return x`.
- **Teaching Notes**: Show that `return` immediately exits the function block.

### Week 3, Session 3: Program Decomposition and Functional Project
- **Week**: 3
- **Session**: 3
- **Topic**: Single-Responsibility Functions & Week 3 Project
- **Duration**: 3 Hours
- **Main Goal**: Students should refactor a procedural CLI program into modular, single-responsibility functions.
- **Required Preparation**: Review clean function separation (`display_menu()`, `add_student()`, `main()`).
- **Learning Objectives**: Students can decompose large programs into focused functions and coordinate them via `main()`.
- **Topics**: Program decomposition, single responsibility principle, CLI menus, Week 3 Functional Student Manager project.
- **Demonstration**: Live code refactoring an inline script into clean `main()` controlled functions.
- **Guided Activity**: Walk through the architectural layout of the Week 3 project.
- **Independent Activity**: Students build `Projects/weekly-projects/week-three/student_management_system.py`.
- **Assessment**: Verify every function in the student's project has a single clear responsibility and docstring.
- **Homework**: Complete Week 3 Learning Checklist and quiz.
- **Common Problems**: Writing 100-line "god functions" that do everything inside `main()`.
- **Teaching Notes**: Remind students that small functions are much easier to test and debug.

---

## Week Four — Strings and Data Persistence

### Week 4, Session 1: Strings in Depth
- **Week**: 4
- **Session**: 1
- **Topic**: String Manipulation, Slicing, and Input Sanitization
- **Duration**: 3 Hours
- **Main Goal**: Students should slice, format, sanitize, and validate string text data.
- **Required Preparation**: Review string methods (`strip`, `upper`, `lower`, `replace`, `split`, `isdigit`).
- **Learning Objectives**: Students can format strings with f-strings and validate text inputs cleanly.
- **Topics**: Indexing, slicing, string methods, f-strings, input validation (`isdigit()`, `isalpha()`).
- **Demonstration**: Live code an input cleaner that trims leading/trailing spaces and capitalizes names properly.
- **Guided Activity**: Complete string sanitization exercises.
- **Independent Activity**: Build a student ID format validator checking prefixes and numeric lengths.
- **Assessment**: Test student code with noisy inputs like `"   sara   "` to verify clean sanitization.
- **Homework**: Read file handling preview for Session 2.
- **Common Problems**: Forgetting that strings are immutable (methods return a new string rather than modifying in-place).
- **Teaching Notes**: Show students how `.strip().title()` chains clean up messy user entries instantly.

### Week 4, Session 2: Text Files and `pathlib`
- **Week**: 4
- **Session**: 2
- **Topic**: Reading and Writing Files with `with open()` & `pathlib`
- **Duration**: 3 Hours
- **Main Goal**: Students should open, read, write, and append text files safely on disk.
- **Required Preparation**: Prepare examples showing file creation and cross-platform path handling using `pathlib.Path`.
- **Learning Objectives**: Students can use context managers (`with open()`) and relative paths to store persistent data.
- **Topics**: Opening/reading/writing/appending files, context managers, relative vs. absolute paths, `pathlib`.
- **Demonstration**: Live code writing a student roster to `students.txt` and reading lines back into Python.
- **Guided Activity**: Build a simple log recorder that appends timestamped notes to a text file.
- **Independent Activity**: Create a daily attendance file writer that records present students.
- **Assessment**: Check that students always use `with open()` so file handles close automatically.
- **Homework**: Review JSON dictionary serialization concepts.
- **Common Problems**: `FileNotFoundError` caused by running scripts from the wrong working directory.
- **Teaching Notes**: Teach students to use `pathlib.Path(__file__).parent` for dependable script-relative file paths.

### Week 4, Session 3: JSON, CSV, and Persistent Applications
- **Week**: 4
- **Session**: 3
- **Topic**: JSON/CSV Serialization & Week 4 Persistent Project
- **Duration**: 3 Hours
- **Main Goal**: Students should save structured records to JSON and CSV files in the Week 4 project.
- **Required Preparation**: Review `json.dump()` / `json.load()` and standard `csv.writer()`.
- **Learning Objectives**: Students can serialize Python lists/dictionaries to JSON and export tabular CSV files.
- **Topics**: JSON objects/arrays, saving/loading JSON, CSV files, Persistent Student Management System project.
- **Demonstration**: Live code saving a list of student dictionaries to `data/students.json` and loading them back.
- **Guided Activity**: Walk through the Week 4 Persistent Student Management System specification.
- **Independent Activity**: Students build `Projects/weekly-projects/week-four/main.py`.
- **Assessment**: Verify the student's project retains added students permanently across application restarts.
- **Homework**: Complete Week 4 Learning Checklist and quiz.
- **Common Problems**: Forgetting `indent=4` in `json.dump()`, resulting in unreadable single-line JSON files.
- **Teaching Notes**: Show students how to inspect generated `.json` and `.csv` files directly in VS Code.

---

## Week Five — Reliable Python Applications

### Week 5, Session 1: Errors and Exception Handling
- **Week**: 1
- **Session**: 1
- **Topic**: Error Categories, `try`/`except`, and Crash Prevention
- **Duration**: 3 Hours
- **Main Goal**: Students should write resilient programs that catch runtime exceptions without crashing.
- **Required Preparation**: Prepare traceback examples and input loops demonstrating `ValueError` handling.
- **Learning Objectives**: Students can identify syntax/runtime/logic errors and wrap risky input inside `try`/`except`.
- **Topics**: Error types, exceptions, `try`, `except`, `else`, `finally`, input validation loops.
- **Demonstration**: Live code an age input loop that catches `ValueError` if the user types letters and prompts again cleanly.
- **Guided Activity**: Build the Error-Safe Calculator exercise.
- **Independent Activity**: Create a resilient file loader that catches `FileNotFoundError` gracefully.
- **Assessment**: Test student scripts by entering letters when numbers are requested—program must not crash.
- **Homework**: Review standard library module imports.
- **Common Problems**: Using bare `except:` instead of catching specific exception types like `except ValueError:`.
- **Teaching Notes**: Emphasize that catching specific errors makes code much easier to debug and maintain.

### Week 5, Session 2: Modules and the Python Standard Library
- **Week**: 5
- **Session**: 2
- **Topic**: Standard Library Modules and Custom Module Imports
- **Duration**: 3 Hours
- **Main Goal**: Students should import standard Python utilities and organize helper code into custom modules.
- **Required Preparation**: Prepare examples using `math`, `datetime`, `random`, and multi-file imports.
- **Learning Objectives**: Students can import standard modules and split application code across multiple `.py` files.
- **Topics**: Modules, `import`, `from ... import`, standard library (`datetime`, `math`), custom helper modules.
- **Demonstration**: Live code creating `student_tools.py` and importing its validation functions into `main.py`.
- **Guided Activity**: Build a modular script that calculates student graduation dates using `datetime`.
- **Independent Activity**: Create a random quiz question picker using Python's `random` module.
- **Assessment**: Verify students can import functions across files without syntax errors.
- **Homework**: Review debugging and logging concepts for Session 3.
- **Common Problems**: Naming local scripts after standard modules (e.g., naming a file `random.py`).
- **Teaching Notes**: Show students how cleaner imports keep entrypoint scripts short and readable.

### Week 5, Session 3: Debugging, Logging, and Project Improvement
- **Week**: 5
- **Session**: 3
- **Topic**: Debugging Tracebacks, Standard `logging`, & Week 5 Project
- **Duration**: 3 Hours
- **Main Goal**: Students should debug tracebacks, configure file loggers, and complete the Week 5 project.
- **Required Preparation**: Review VS Code breakpoints and standard `logging.basicConfig()`.
- **Learning Objectives**: Students can use interactive debugger tools and record diagnostic logs to `system.log`.
- **Topics**: Traceback reading, VS Code debugger, breakpoints, standard `logging` module, Week 5 project.
- **Demonstration**: Live code setting up `logger_config.py` to write info and error events to `logs/system.log`.
- **Guided Activity**: Walk through the Week 5 Reliable Student Management System architecture.
- **Independent Activity**: Students build `Projects/weekly-projects/week-five/main.py` with custom tools and logging.
- **Assessment**: Check that student project logs startup events and input errors to `logs/system.log`.
- **Homework**: Complete Week 5 Learning Checklist and quiz.
- **Common Problems**: Using `print()` everywhere for error logging instead of formal `logging.info/error`.
- **Teaching Notes**: Show how logs provide a permanent audit history of application events.

---

## Week Six — Object-Oriented Programming

### Week 6, Session 1: Classes and Objects
- **Week**: 6
- **Session**: 1
- **Topic**: Object-Oriented Principles, Classes, Objects, and `__init__`
- **Duration**: 3 Hours
- **Main Goal**: Students should define custom class blueprints and instantiate independent objects.
- **Required Preparation**: Prepare diagrams showing class blueprints vs. individual object instances.
- **Learning Objectives**: Students can define a class, initialize attributes via `__init__`, and use `self`.
- **Topics**: OOP concepts, class definitions, object instantiation, `__init__()`, `self`, instance attributes/methods.
- **Demonstration**: Live code a `Student` class with `name` and `score` attributes, and instantiate two student objects.
- **Guided Activity**: Complete basic class definition exercises.
- **Independent Activity**: Build a `Course` class that tracks course title, instructor name, and credit hours.
- **Assessment**: Verify students understand that `self` refers to the specific object instance being operated on.
- **Homework**: Practice adding instance methods to custom classes.
- **Common Problems**: Forgetting `self` as the first parameter in class methods (`def get_name():`).
- **Teaching Notes**: Use real-world analogies (cookie cutter = class, cookie = object) to clarify OOP.

### Week 6, Session 2: Building Class-Based Applications
- **Week**: 6
- **Session**: 2
- **Topic**: Object Collections, Controller Classes, and Serialization
- **Duration**: 3 Hours
- **Main Goal**: Students should manage lists of objects and implement `to_dict()` dictionary serialization.
- **Required Preparation**: Review coordinating controller classes (`StudentManager`) and JSON conversion.
- **Learning Objectives**: Students can store objects inside lists and convert object attributes to dictionaries.
- **Topics**: Object collections, updating object attributes, dictionary serialization (`to_dict`/`from_dict`), class responsibilities.
- **Demonstration**: Live code a `StudentManager` class that stores `Student` objects and converts them to JSON format.
- **Guided Activity**: Build an object-based classroom roster controller.
- **Independent Activity**: Create a book library manager using `Book` and `Library` classes.
- **Assessment**: Check that students keep domain data inside `Student` and menu control inside `StudentManager`.
- **Homework**: Review basic class inheritance concepts.
- **Common Problems**: Trying to `json.dump()` custom Python objects directly without converting to dictionaries first.
- **Teaching Notes**: Explain separation of concerns: domain models hold data; controller classes manage operations.

### Week 6, Session 3: Basic Inheritance and OOP Project
- **Week**: 6
- **Session**: 3
- **Topic**: Parent/Child Inheritance & Week 6 OOP Project
- **Duration**: 3 Hours
- **Main Goal**: Students should implement class inheritance and complete the Week 6 OOP Student Management project.
- **Required Preparation**: Review parent classes, child classes, and `super().__init__()`.
- **Learning Objectives**: Students can inherit attributes/methods from a parent class and structure OOP applications.
- **Topics**: Base classes, child classes, basic inheritance, `super()`, Week 6 OOP Student Management System project.
- **Demonstration**: Live code a `User` parent class and a `Student(User)` child class extending it with academic major.
- **Guided Activity**: Walk through the Week 6 Object-Oriented Student Management System specification.
- **Independent Activity**: Students build `Projects/weekly-projects/week-six/main.py`.
- **Assessment**: Verify student project cleanly uses class encapsulation and basic inheritance.
- **Homework**: Complete Week 6 Learning Checklist and quiz.
- **Common Problems**: Overcomplicating inheritance hierarchies with unnecessary multiple inheritance levels.
- **Teaching Notes**: Keep inheritance simple and beginner-friendly—one parent class to one child class.

---

## Week Seven — Python Development Tools

### Week 7, Session 1: Virtual Environments and Packages
- **Week**: 7
- **Session**: 1
- **Topic**: Python Package Management (`pip`) & Virtual Environments (`venv`)
- **Duration**: 3 Hours
- **Main Goal**: Students should create isolated virtual environments and install third-party packages cleanly.
- **Required Preparation**: Review terminal commands for `python -m venv .venv` across Linux, macOS, and Windows.
- **Learning Objectives**: Students can create/activate a virtual environment, install packages via `pip`, and freeze `requirements.txt`.
- **Topics**: Third-party packages, PyPI, `pip`, virtual environments (`venv`), environment activation, `requirements.txt`.
- **Demonstration**: Live code creating `.venv`, activating it, installing `requests`, and exporting `pip freeze > requirements.txt`.
- **Guided Activity**: Students set up an isolated virtual environment for their Week 7 project folder.
- **Independent Activity**: Create a clean environment and test installing a utility package.
- **Assessment**: Check student terminal prompts for `(.venv)` to verify active virtual environment status.
- **Homework**: Review Git version control commands for Session 2.
- **Common Problems**: Installing packages globally without activating `.venv` first.
- **Teaching Notes**: Explain why virtual environments prevent dependency version conflicts between projects.

### Week 7, Session 2: Git and GitHub
- **Week**: 7
- **Session**: 2
- **Topic**: Version Control with Git, `.gitignore`, and GitHub
- **Duration**: 3 Hours
- **Main Goal**: Students should initialize a local Git repository, commit changes, and push code to GitHub.
- **Required Preparation**: Ensure Git is installed and student GitHub accounts are active.
- **Learning Objectives**: Students can use `git init/status/add/commit/push` and configure `.gitignore` safety rules.
- **Topics**: Version control concepts, Git commands, commit snapshots, `.gitignore`, GitHub repositories, `push`/`pull`.
- **Demonstration**: Live code initializing a repository, adding `.gitignore`, committing initial code, and pushing to GitHub.
- **Guided Activity**: Students initialize Git for their project and configure a proper `.gitignore` file.
- **Independent Activity**: Push a sample repository to GitHub and inspect the online file tree.
- **Assessment**: Verify that no student accidentally commits `.venv/` or `__pycache__/` folders to GitHub.
- **Homework**: Review multi-file project architecture for Session 3.
- **Common Problems**: Forgetting to run `git add .` before running `git commit`.
- **Teaching Notes**: Emphasize commit message clarity and never committing passwords or API keys.

### Week 7, Session 3: Project Structure and Clean Code
- **Week**: 7
- **Session**: 3
- **Topic**: Multi-File Package Structure & Week 7 Project
- **Duration**: 3 Hours
- **Main Goal**: Students should structure a multi-file Python package and complete the Week 7 project.
- **Required Preparation**: Review professional folder structures (`models/`, `services/`, `utilities/`).
- **Learning Objectives**: Students can organize code into packages with `__init__.py` and use clean entrypoints (`main.py`).
- **Topics**: Multi-file packages, separation of concerns, `__init__.py`, docstrings, Week 7 Professionally Organized Project.
- **Demonstration**: Live code splitting a single-file application into `models/student.py`, `services/student_manager.py`, and `main.py`.
- **Guided Activity**: Walk through the Week 7 Professionally Organized Student Management System structure.
- **Independent Activity**: Students build `Projects/weekly-projects/week-seven/` modular package architecture.
- **Assessment**: Verify student project runs cleanly from `python main.py` with separated domain and service modules.
- **Homework**: Complete Week 7 Learning Checklist and quiz.
- **Common Problems**: Circular import errors caused by two modules importing each other directly.
- **Teaching Notes**: Show students how clean package organization makes code professional and easy to navigate.

---

## Week Eight — APIs, Testing, and Capstone Development

### Week 8, Session 1: Working With APIs
- **Week**: 8
- **Session**: 1
- **Topic**: REST APIs, HTTP Requests, and JSON Response Parsing
- **Duration**: 3 Hours
- **Main Goal**: Students should fetch and parse live JSON data from external REST APIs using `requests`.
- **Required Preparation**: Prepare public API endpoint URLs that do not require complex authentication keys.
- **Learning Objectives**: Students can make GET requests, verify HTTP status codes (`200`), and parse JSON responses.
- **Topics**: REST APIs, HTTP methods, URLs/endpoints, status codes (`200`, `404`), `requests.get()`, JSON parsing.
- **Demonstration**: Live code a script fetching data from a public API endpoint and formatting results cleanly.
- **Guided Activity**: Complete API inspection exercises.
- **Independent Activity**: Build a CLI utility that fetches and displays live information from a public web API.
- **Assessment**: Verify students check `response.status_code == 200` before parsing JSON payloads.
- **Homework**: Review automated unit testing concepts for Session 2.
- **Common Problems**: Network timeout errors or attempting to parse HTML error pages as JSON.
- **Teaching Notes**: Remind students to handle connection errors gracefully with `try`/`except requests.exceptions.RequestException`.

### Week 8, Session 2: Introduction to Automated Testing
- **Week**: 8
- **Session**: 2
- **Topic**: Automated Unit Testing with Python's `unittest` Framework
- **Duration**: 3 Hours
- **Main Goal**: Students should write automated unit test cases verifying functions and classes.
- **Required Preparation**: Review `unittest.TestCase`, test method naming (`test_*`), and assertion methods (`assertEqual`).
- **Learning Objectives**: Students can write unit tests, run test discovery, and interpret test pass/fail output.
- **Topics**: Why testing matters, manual vs. automated tests, `unittest`, test cases, assertions (`assertEqual`, `assertTrue`).
- **Demonstration**: Live code writing a unit test suite for a math utility function and running it from the terminal.
- **Guided Activity**: Write unit tests for domain models and calculation functions.
- **Independent Activity**: Build automated unit test cases for their chosen final capstone project.
- **Assessment**: Verify students execute `python -m unittest discover tests` and achieve clean `OK` test runs.
- **Homework**: Finalize capstone project code and documentation for Session 3 presentation.
- **Common Problems**: Forgetting to prefix test method names with `test_`, causing `unittest` to skip them.
- **Teaching Notes**: Show how automated tests act as a safety net when refactoring or adding new features.

### Week 8, Session 3: Capstone Project Showcase
- **Week**: 8
- **Session**: 3
- **Topic**: Capstone Project Finalization, Code Review & Presentation
- **Duration**: 3 Hours
- **Main Goal**: Students should demonstrate their completed capstone software project and explain its architecture.
- **Required Preparation**: Prepare project presentation schedule, projector setup, and 100-point Project Rubric sheets.
- **Learning Objectives**: Students can present technical solutions, demonstrate live software features, and articulate design decisions.
- **Topics**: Capstone project demonstration, technical communication, code walkthrough, course review and graduation.
- **Demonstration**: Instructor models a concise 5-minute technical project walkthrough highlighting structure and features.
- **Guided Activity**: Final pre-presentation peer testing and README audit.
- **Independent Activity**: Students present their capstone project (Student Management, Contact Book, Expense Tracker, Quiz App, or To-Do List).
- **Assessment**: Complete formal grading using the 100-point Final Project Evaluation Rubric.
- **Homework**: Celebrate completing the 8-week Python Beginner to Practical Developer Roadmap!
- **Common Problems**: Presentation anxiety or trying to show every single line of code instead of highlighting architecture.
- **Teaching Notes**: Celebrate student growth—compare their Week 1 `print()` scripts to their Week 8 tested capstone packages!
