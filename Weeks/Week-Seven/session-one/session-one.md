# 📘 Week Seven – Session One: Virtual Environments and Python Packages

Welcome back! 👋

Up until now, every single script and project you built relied exclusively on Python's **built-in syntax** and the **Standard Library** (`math`, `random`, `json`, `csv`).

However, one of Python's greatest superpowers is its community ecosystem! Over half a million free third-party packages exist on the **Python Package Index (PyPI)**—ready to help you connect to web APIs, analyze data, or build graphical interfaces.

But there is a catch: if you install hundreds of packages globally on your computer, projects will eventually clash over different package versions. In this session, you will learn how to use **`pip`** to manage packages, isolate project dependencies inside **Virtual Environments** (`venv`), lock versions using **`requirements.txt`**, and set up our practical activity project!

---

## 🎯 Learning Objectives

By the end of this session, you will be able to:
- Explain what external Python packages are and how they differ from the Standard Library
- Check your `pip` version and install, list, and remove packages via terminal
- Explain why global installations cause version conflicts across projects
- Create, activate, and deactivate project-specific virtual environments (`.venv`) across OS platforms
- Generate and restore dependency files using `pip freeze` and `requirements.txt`
- Troubleshoot common terminal and environment activation problems
- Set up isolated project structures ready for professional software development

---

## 📌 1. Introduction: Why Isolate Dependencies?

Imagine you build **Project A** in 2024 using `requests` version 2.25. Two years later, you start **Project B** which requires `requests` version 3.0.

If you upgrade `requests` globally on your laptop, **Project A** might suddenly break!

> **Professional rule**: Every Python project should have its own isolated container of installed packages so changing one project never breaks another.

---

## 📦 2. What Is a Package?

A **Package** is a folder of reusable Python modules written by other developers that you can download and import into your own scripts.
- **Standard Library**: Built into Python automatically (`os`, `json`, `csv`, `logging`).
- **External Packages**: Downloaded from the internet via PyPI (`requests`, `pytest`, `flask`).

---

## 🛠️ 3. What Is `pip`?

**`pip`** is Python's official package installer. Let us check if `pip` is ready on your system by running this command in your terminal:

```bash
python -m pip --version
```

### Example Output:
```text
pip 24.0 from /usr/lib/python3.11/site-packages/pip (python 3.11)
```

*(Note: Always run `pip` using `python -m pip` to guarantee you are using the installer attached to your active Python interpreter!)*

---

## ➕ 4. Installing a Package

To install a package from PyPI, run `python -m pip install <package_name>`:

```bash
python -m pip install requests
```

🔍 **Breakdown**:
- `python -m`: Runs a Python module as a command-line script.
- `pip`: Tells Python to invoke the package manager.
- `install requests`: Downloads and installs the `requests` HTTP library.

---

## 📋 5. Viewing Installed Packages

To inspect all packages currently installed in your active environment:

```bash
python -m pip list
```

---

## 🗑️ 6. Removing a Package

To uninstall a package you no longer need:

```bash
python -m pip uninstall requests
```

---

## 🌐 7. What Is a Virtual Environment?

A **Virtual Environment** (`venv`) is like an isolated private room for your project.

Imagine an apartment building. Instead of sharing one kitchen shelf with 50 neighbors (global installation), every apartment gets its own private refrigerator! When you activate a project's virtual environment, any package you install with `pip` goes strictly into that project's `.venv` folder.

---

## 🏗️ 8. Creating a Virtual Environment

To create a virtual environment named `.venv` inside your project folder:

```bash
python -m venv .venv
```

This creates a hidden directory named `.venv/` containing an isolated copy of Python and `pip`.

---

## 🔌 9. Activating a Virtual Environment

Before installing packages, you **must activate** your virtual environment! The exact terminal command depends on your Operating System:

### Linux / macOS (Bash / Zsh):
```bash
source .venv/bin/activate
```

### Windows (PowerShell):
```powershell
.venv\Scripts\Activate.ps1
```

### Windows (Command Prompt `cmd.exe`):
```cmd
.venv\Scripts\activate
```

When activated successfully, your terminal prompt will display the environment name in parentheses at the far left:
```text
(.venv) user@computer:~/my-project$
```

---

## 🛑 10. Deactivating

When you finish working on your project, simply run:

```bash
deactivate
```

Your prompt will return to normal, and you will be back in your global system environment.

---

## 🔒 11. Locking Dependencies (`requirements.txt`)

When sharing a project on GitHub, you **never** upload the heavy `.venv/` folder! Instead, you generate a text file listing all installed package versions:

### Save installed package list to `requirements.txt`:
```bash
python -m pip freeze > requirements.txt
```

### Example content of `requirements.txt`:
```text
certifi==2024.2.2
charset-normalizer==3.3.2
idna==3.6
requests==2.31.0
urllib3==2.2.1
```

### Install all dependencies from `requirements.txt` on a new computer:
```bash
python -m pip install -r requirements.txt
```

---

## 🛠️ 12. Practical Activity: Weather Project Environment Setup

Let us set up a clean, isolated project structure for a future weather or API application!

### Step 1: Create project folder
```bash
mkdir weather-project
cd weather-project
```

### Step 2: Create and activate virtual environment
```bash
python -m venv .venv
source .venv/bin/activate  # Or Windows equivalent
```

### Step 3: Install `requests` package
```bash
python -m pip install requests
```

### Step 4: Create starter `main.py`
Create `main.py` and test our imported package:

```python
# main.py
import requests

print("✅ 'requests' package imported successfully inside virtual environment!")
print("Requests version:", requests.__version__)
```

### Step 5: Save `requirements.txt`
```bash
python -m pip freeze > requirements.txt
```

Your clean project structure now looks like this:
```text
weather-project/
│
├── .venv/              <-- Isolated environment (ignored by Git)
├── main.py             <-- Application entry point
└── requirements.txt    <-- Locked dependency list
```

---

## ⚠️ 13. Common Terminal & Environment Problems

| Problem | Cause | Solution |
| :--- | :--- | :--- |
| **`python: command not found`** | Python is not added to system PATH | On Windows, reinstall Python and check ✅ **Add Python to PATH**. Or try `python3`. |
| **`No module named pip`** | `pip` was not installed with Python | Run `python -m ensurepip --upgrade`. |
| **Environment not activating** | Execution policy blocked on PowerShell | Run PowerShell as Admin: `Set-ExecutionPolicy Unrestricted -Scope Process`. |
| **`ModuleNotFoundError` after install** | Package was installed in global environment while `.venv` was inactive | Check terminal prompt for `(.venv)`, activate environment, and run `pip install` again. |

---

## 📝 14. Practice Exercises

Try these commands on your own terminal!

### Beginner
1. **Check Versions**: Open your terminal and run `python --version` and `python -m pip --version`.
2. **Create Environment**: Create a practice directory named `test-env`, navigate into it, and run `python -m venv .venv`.

### Intermediate
3. **Activate & Inspect**: Activate `.venv` and run `python -m pip list`. Notice how clean and empty an isolated environment is compared to global Python!
4. **Freeze & Restore**: Install any small package (e.g., `python -m pip install colorama`), freeze it to `requirements.txt`, inspect the text file, and uninstall `colorama`.

### Challenge
5. **Recreate From Requirements**: Run `python -m pip install -r requirements.txt` and verify using `pip list` that `colorama` was automatically restored!

---

## ❓ 15. Review Questions

1. Why is installing packages globally across all projects risky?
2. Why should you use `python -m pip install` instead of running `pip install` directly?
3. What visual cue in your command line tells you that a virtual environment is active?
4. Why do we exclude the `.venv/` folder when sharing projects on GitHub?
5. What terminal command installs all dependencies listed inside `requirements.txt`?

---

## ✅ 16. Learning Checklist

- [ ] I can check Python and `pip` versions from my terminal.
- [ ] I can install, list, and uninstall third-party packages.
- [ ] I can create isolated virtual environments (`.venv`).
- [ ] I can activate and deactivate virtual environments across operating systems.
- [ ] I can generate and restore dependency lists using `requirements.txt`.

---

## 🏁 17. Session Summary

- **Third-Party Packages** extend Python's capabilities beyond the built-in Standard Library.
- **Virtual Environments (`venv`)** isolate packages per project to prevent version collisions.
- **`requirements.txt`** locks exact package versions so any collaborator can reproduce your environment effortlessly.
