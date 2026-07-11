# 🌿 Git and GitHub Cheat Sheet

Version control is an essential skill for practical developers. This cheat sheet gives you quick commands and workflows for tracking your Python projects with Git and sharing them safely on GitHub.

---

## Git Versus GitHub

| Feature | Git | GitHub |
| --- | --- | --- |
| **What It Is** | Version control software installed locally on your computer | Online cloud platform for storing and sharing Git repositories |
| **Where It Runs** | Locally on your machine | On the web (`github.com`) |
| **Main Purpose** | Tracks code history, snapshots, and local branches | Backup, collaboration, project publishing, and code review |

---

## Check Git Installation

Verify that Git is installed on your computer:

```bash
git --version
```

---

## Configure Git

Set your identity so your commits are attributed correctly:

```bash
git config --global user.name "Your Name"
```

```bash
git config --global user.email "your-email@example.com"
```

---

## Create a Repository

Initialize a new local Git repository inside your project folder:

```bash
git init
```

---

## Check Status

Inspect which files have been modified, staged, or are untracked:

```bash
git status
```

---

## Add Files

Stage files so they are ready to be included in your next commit snapshot:

### Stage a Single File
```bash
git add main.py
```

### Stage All Changes in the Directory
```bash
git add .
```

---

## Commit Changes

Save a permanent snapshot of your staged changes with a descriptive message:

```bash
git commit -m "Add student search feature"
```

### Writing Good Commit Messages
Always write clear, action-oriented commit messages explaining **what** changed:

- **Good Commit Messages**:
  ```text
  Add student search feature
  Fix invalid score validation
  Create project README
  ```
- **Avoid Vague Messages**:
  ```text
  update
  stuff
  final final
  ```

---

## View History

Review past commit snapshots and author history:

```bash
git log
```

View a compact, one-line summary of commit history:

```bash
git log --oneline
```

---

## Connect to GitHub

Link your local repository to an empty repository created on GitHub:

```bash
git remote add origin <repository-url>
```

---

## Push

Rename your primary branch to `main` and push your commits up to GitHub:

```bash
git branch -M main
```

```bash
git push -u origin main
```

---

## Pull

Download and merge latest changes from your remote GitHub repository:

```bash
git pull
```

---

## Clone

Download a complete copy of an existing remote GitHub repository to your computer:

```bash
git clone <repository-url>
```

---

## Branch Basics

Branches let you work on new features safely without affecting your main working code:

### List All Local Branches
```bash
git branch
```

### Create and Switch to a New Feature Branch
```bash
git switch -c feature-name
```

### Switch Back to Main Branch
```bash
git switch main
```

---

## `.gitignore`

A `.gitignore` file tells Git which files or folders it should automatically ignore and never upload to GitHub:

### Example `.gitignore`
```gitignore
.venv/
__pycache__/
*.pyc
.env
logs/
.vscode/
```

> **CRITICAL SAFETY RULE**: Never upload secrets, `.env` files, or your `.venv/` virtual environment folder!

---

## Common Git Workflow

Follow this standard workflow every time you make progress on your project:

```text
Edit code files
     ↓
git status
     ↓
git add .
     ↓
git commit -m "Describe what changed"
     ↓
git push
```

---

## Common Problems & Simple Solutions

- **Nothing to commit**: You ran `git commit` before running `git add .`, or no files were changed since your last commit.
- **Remote origin already exists**: You ran `git remote add origin` twice. Use `git remote set-url origin <new-url>` if updating the URL.
- **Push rejected**: Someone pushed changes to GitHub ahead of you. Run `git pull` first, resolve any conflicts, then push again.
- **Wrong branch**: Check `git branch` to see where you are, then use `git switch main` to return to your main branch.
- **File not tracked**: You created a new file but forgot to stage it with `git add .`.
- **Accidentally added `.venv`**: Create your `.gitignore` file listing `.venv/`, then run `git rm -r --cached .venv` to unstage it before committing.

---

## Git Safety Checklist

NEVER commit or push any of the following items to GitHub:
- Passwords or database connection strings
- API keys or secret authentication tokens
- `.env` configuration files containing private credentials
- Private personal information or student records
- Large virtual environment directories (`.venv/`)
