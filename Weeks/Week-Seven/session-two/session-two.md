# 📘 Week Seven – Session Two: Git and GitHub

Welcome back! 👋

Have you ever worked on a school assignment or project where your folder ended up looking like this?
```text
Final_Project.py
Final_Project_v2.py
Final_Project_v3_fixed.py
Final_Project_ACTUAL_FINAL.py
```

Or worse—have you ever deleted a block of working code accidentally, saved the file, and realized you had no way to undo your change?

Professional software engineers solve this problem using **Version Control**. In this session, you will learn how to track every single edit to your codebase using **Git**, synchronize your repositories in the cloud using **GitHub**, ignore temporary environment folders using **`.gitignore`**, and publish your Python projects to the world!

---

## 🎯 Learning Objectives

By the end of this session, you will be able to:
- Explain what version control is using beginner-friendly analogies
- Distinguish between Git (local version tracking tool) and GitHub (cloud repository hosting)
- Check Git installation and configure global author identity (`user.name`, `user.email`)
- Initialize local Git repositories (`git init`) and inspect tracking status (`git status`)
- Stage specific files or entire directories (`git add`) and record checkpoints (`git commit`)
- Connect local repositories to remote GitHub servers (`git remote add origin`) and push commits
- Clone remote repositories (`git clone`) and fetch upstream updates (`git pull`)
- Write `.gitignore` rules to prevent uploading `.venv/` and cache files

---

## 📌 1. Introduction: What Is Version Control?

Think of **Version Control** like a save-game checkpoint system in a video game.

Before taking on a difficult boss fight, you save your progress. If things go wrong, you reload your checkpoint! Similarly, **Git** records snapshots (commits) of your project over time so you can inspect history, undo mistakes, or experiment without fear.

---

## 🛠️ 2. What Is Git?

**Git** is a free, open-source command-line tool installed directly on your computer that tracks modifications across files over time.

---

## 🌐 3. What Is GitHub?

**GitHub** is a cloud website where developers host their Git repositories online.

> 💡 **Git vs. GitHub**:
> - **Git** is the engine running on your laptop.
> - **GitHub** is the online library where you store and share your Git repositories.

---

## 🔍 4. Check Your Git Installation

Open your terminal and verify that Git is installed:

```bash
git --version
```

### Example Output:
```text
git version 2.43.0
```

---

## ⚙️ 5. Configure Your Git Identity

Before making your first checkpoint, tell Git your name and email. Replace the examples below with your own real name and email address:

```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

---

## 📁 6. Create a Local Repository (`git init`)

To start tracking an existing project folder (for example, `weather-project`), navigate into it and run:

```bash
git init
```

This creates a hidden `.git/` folder containing your project's version history engine.

---

## 📊 7. Check Repository Status (`git status`)

To see which files are modified, staged, or untracked at any moment:

```bash
git status
```

---

## ➕ 8. Stage Files (`git add`)

Before recording a checkpoint, you must select which files to include. This is called **Staging**:

```bash
# Stage a single specific file
git add main.py

# Stage all modified and new files in the folder
git add .
```

---

## 📸 9. Commit Checkpoints (`git commit`)

A **Commit** saves a permanent snapshot of your staged files along with a descriptive message explaining what changed:

```bash
git commit -m "Create student management project"
```

### Tips for Writing Good Commit Messages:
- Use clear, descriptive action verbs (`Add search feature`, `Fix division error`).
- Avoid vague messages like `update code` or `fixed stuff`.

---

## 📜 10. View Commit History (`git log`)

To review the chronological timeline of all your previous commits:

```bash
git log
```

---

## ☁️ 11. Publishing to GitHub

To publish your local repository to GitHub:
1. Log into GitHub and click **New Repository**.
2. Give your repository a name (do not check "Initialize with README" if your local folder already has files).
3. Copy the repository URL (`https://github.com/username/repository-name.git`).
4. Run the following terminal commands inside your project folder:

```bash
# Link your local folder to your remote GitHub repository
git remote add origin <repository-url>

# Ensure your default branch is named 'main'
git branch -M main

# Upload your commits to GitHub
git push -u origin main
```

---

## 📥 12. Cloning a Remote Repository (`git clone`)

To download a complete copy of any public repository from GitHub onto your computer:

```bash
git clone <repository-url>
```

---

## 🔄 13. Pulling Latest Changes (`git pull`)

If a collaborator pushes new updates to GitHub, download and merge them into your local folder using:

```bash
git pull
```

---

## 🛡️ 14. Excluding Files (`.gitignore`)

Remember Week Seven Session One? We created a `.venv/` virtual environment folder. **You should never upload `.venv/` or Python cache files to GitHub!**

Create a text file named `.gitignore` in your project root:

```gitignore
# Virtual environments
.venv/
venv/
env/

# Python compiled bytecode cache
__pycache__/
*.pyc

# OS system files
.DS_Store
```

Any file or folder listed inside `.gitignore` is completely ignored by `git status` and `git add .`!

---

## 🛠️ 15. Practical Activity: Publish Your Python Project

Let us publish your `weather-project` (or Student Management System) to GitHub:
1. Create `.gitignore` and add `.venv/` and `__pycache__/`.
2. Run `git init`.
3. Run `git status` to verify `.venv/` is hidden!
4. Stage files: `git add .`
5. Commit snapshot: `git commit -m "Initial project release"`
6. Create a GitHub repository and push your code using `git remote add origin ...` and `git push -u origin main`.

---

## ⚠️ 16. Common Git Problems & Basic Fixes

| Problem | Explanation & Fix |
| :--- | :--- |
| **`fatal: not a git repository`** | You ran a Git command outside a folder initialized with `git init`. Navigate into your project directory first (`cd my-project`). |
| **`Please tell me who you are`** | You forgot to run `git config --global user.name` and `user.email`. |
| **Accidentally staged `.venv/`** | If you forgot `.gitignore` and ran `git add .`, unstage it using `git rm -r --cached .venv`. |

---

## 📝 17. Practice Exercises

Try these Git workflows on your local machine!

### Beginner
1. **Initialize & Status**: Create a practice folder named `git-practice`, run `git init`, create a file named `notes.txt`, and check `git status`.
2. **Stage & Commit**: Stage `notes.txt` using `git add notes.txt` and commit it with `git commit -m "Add practice notes"`.

### Intermediate
3. **Ignore Rules**: Create a `.gitignore` file excluding `secret.txt`. Create `secret.txt` and verify that `git status` completely ignores it!
4. **Log Inspection**: Make two more edits and commits, then run `git log` to inspect your 3-commit history timeline.

### Challenge
5. **Remote Collaboration**: Create a private repository on GitHub, push your `git-practice` folder to it, and verify that your files appear online!

---

## ❓ 18. Review Questions

1. What is the difference between Git and GitHub?
2. What terminal command initializes a new local Git repository?
3. Why must you stage files (`git add`) before committing them (`git commit`)?
4. What is the purpose of the `-m` flag in `git commit -m "..."`?
5. Why should virtual environment folders (`.venv/`) be listed inside `.gitignore`?

---

## ✅ 19. Learning Checklist

- [ ] I can explain the difference between Git and GitHub.
- [ ] I can initialize local repositories (`git init`) and check file status (`git status`).
- [ ] I can stage files (`git add .`) and record descriptive commits (`git commit -m`).
- [ ] I can link local folders to GitHub and push changes online.
- [ ] I can use `.gitignore` to prevent uploading virtual environments and cache files.

---

## 🏁 20. Session Summary

- **Git** tracks local file modifications and allows safe checkpoint snapshots.
- **GitHub** hosts Git repositories securely in the cloud for collaboration.
- **`.gitignore`** protects repositories from being cluttered by heavy `.venv/` directories.
