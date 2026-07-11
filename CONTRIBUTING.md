# 🤝 Contributing to the Python Beginner Roadmap

## 1. Welcome

Thank you for helping improve the **Python Beginner to Practical Developer Roadmap**.

We welcome contributions from students, instructors, Python developers, technical writers, curriculum designers, and open-source contributors. Your contributions help improve:
- Lessons and explanations
- Code examples
- Exercises and starter files
- Runnable weekly and capstone projects
- Repository documentation
- Student resources (`Student-Resources/`)
- Instructor resources (`Instructor-Guide/`)
- Accessibility and readability
- Bug fixes and corrections

---

## 2. Ways to Contribute

You can contribute in many ways, including:
- Fix spelling or grammar errors
- Improve conceptual explanations
- Report broken links or missing files
- Fix incorrect or buggy code examples
- Add beginner-friendly examples
- Improve student exercises and practice prompts
- Improve project documentation and reference code
- Improve student cheat sheets and checklists
- Improve instructor lesson plans and rubrics
- Suggest accessibility improvements
- Report technical problems or environment setup issues

> **Note**: Major curriculum changes should be discussed before implementation by opening an issue first.

---

## 3. Before Contributing

Before writing code or editing documentation, please complete this checklist:

```text
[ ] Read the root README.md
[ ] Review the eight-week course structure
[ ] Find the relevant week and session folder
[ ] Check whether a similar contribution or issue already exists
[ ] Preserve the beginner learning order
[ ] Avoid adding advanced concepts too early
[ ] Test code changes locally
```

---

## 4. Curriculum Contribution Rules

All curriculum contributions must:
- Remain beginner-friendly and encouraging
- Follow the approved eight-week, 24-session course structure
- Preserve pedagogical topic order
- Use clear, straightforward English
- Use relatable, practical examples (e.g., student gradebooks, contact lists)
- Avoid unnecessary technical complexity
- Match the author's existing friendly instructor writing style

### Pedagogical Order Rules
Do not introduce advanced concepts before students learn the required foundations:
- **Week One** should not use functions (`def`), lists, classes, or exception handling (`try`/`except`).
- **Week Two** should not depend on custom functions or Object-Oriented classes.
- Always check what topics have been introduced up to the specific session you are editing.

---

## 5. Writing Style

When writing lessons, exercises, or documentation:
- Maintain a friendly, supportive instructor tone
- Keep explanations concise and practical
- Provide clear, well-commented examples
- Use descriptive, beginner-readable variable names
- Follow existing GitHub-flavored Markdown conventions

### Naming Best Practices
- **Prefer descriptive names**:
  ```python
  student_name = "Sara"
  student_list = ["Sara", "Abebe", "Mahi"]
  ```
- **Avoid cryptic shortcuts**:
  ```python
  n = "Sara"
  arr = ["Sara", "Abebe", "Mahi"]
  ```

Avoid writing like academic textbooks or dense corporate API specifications.

---

## 6. Code Contribution Rules

All Python code contributed to this repository must:
- Run cleanly on Python 3
- Follow valid Python syntax and standard 4-space indentation
- Use descriptive variable, function, and class names
- Align strictly with the concepts taught in that session
- Avoid unnecessary external dependencies
- Avoid clever shortcuts that confuse beginners

### Patterns to Avoid in Beginner Lessons
Unless editing advanced or extension topics intentionally, avoid:
- Complex nested list/dict comprehensions
- Lambda-heavy code pipelines
- Advanced decorators or metaclasses
- Asynchronous programming (`async`/`await`)
- Overly complex architectural patterns

---

## 7. Security and Privacy

Never commit sensitive credentials or private information:

```text
Passwords
API keys
Access tokens
Connection strings
Private student information
Real grades
Personal addresses
Private phone numbers
Private email information
.env files
```

Always use fictional sample information:
- Use `student@example.com` instead of real email addresses.
- Use fictional names (`Sara`, `Abebe`, `Mahi`) and placeholder IDs (`STU-001`).

---

## 8. Repository Setup

To set up the repository locally:

```bash
git clone <repository-url>
cd Python-Begginer-Roadmap
```

*(Replace `<repository-url>` with the official repository clone URL.)*

---

## 9. Create a Branch

Always create an isolated feature branch for your work:

```bash
git switch -c improve-week-two-exercises
```

Use descriptive branch names, such as:
```text
fix-week-one-typo
improve-json-explanation
add-git-practice-activity
```

---

## 10. Make Changes

When making edits:
- Keep your changes focused on a single topic or fix
- Do not modify unrelated files
- Preserve existing folder structure and file names
- Test all code examples after modifying them
- Check all internal Markdown links

---

## 11. Validate Changes

Before committing your changes, validate that Python source code compiles cleanly:

```bash
python -m compileall Weeks Projects
```

Also verify:
- Interactive scripts start and exit properly
- Python syntax is valid
- Markdown headings and code blocks are formatted correctly
- Relative links resolve accurately
- JSON files (`data/*.json`) are valid syntax
- CSV files contain proper column headers

---

## 12. Commit Changes

Stage and commit your changes with a clear, meaningful commit message:

```bash
git add .
git commit -m "Improve Week Four JSON explanation"
```

---

## 13. Submit Changes

Follow the standard pull request workflow:

```text
Push branch
   ↓
Open pull request
   ↓
Explain changes
   ↓
Respond to review
```

---

## 14. Pull Request Guidelines

When opening a Pull Request, describe:
- What changed?
- Why was it changed?
- Which lesson, week, or resource is affected?
- How was the change tested?
- Are screenshots or terminal outputs needed?

### Pull Request Checklist
Include this verification checklist in your pull request description:

```text
[ ] My contribution matches the course level
[ ] I tested Python code
[ ] I checked Markdown formatting
[ ] I used fictional data
[ ] I did not include secrets
[ ] I updated documentation when necessary
```

---

## 15. Reporting Problems

If you discover a bug or broken example, open an issue including:
- Clear description of the problem
- Exact file path (e.g., `Weeks/Week-Four/session-three/session-three.md`)
- Expected behavior
- Actual behavior
- Error message or traceback (if applicable)
- Suggested improvement

Do not include private student data or credentials in bug reports.

---

## 16. Responsible AI Use

AI tools may be used by contributors as writing or debugging assistants to:
- Review grammar and readability
- Explain confusing traceback messages
- Suggest beginner-friendly practice examples
- Spot syntax or formatting errors

**Contributor Responsibility**:
Contributors must review all AI-generated content, test all generated code, verify accuracy, preserve course writing style, and never submit content or code they do not fully understand.
