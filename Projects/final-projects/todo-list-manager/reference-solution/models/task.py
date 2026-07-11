"""
Task Domain Model
"""

class Task:
    def __init__(self, task_id, title, description, due_date, priority, completed=False):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = completed

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "priority": self.priority,
            "completed": self.completed
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["task_id"],
            data["title"],
            data["description"],
            data["due_date"],
            data["priority"],
            data.get("completed", False)
        )

    def __str__(self):
        status = "✅ DONE" if self.completed else "⏳ PENDING"
        return f"[{self.task_id}] {status} | {self.title:<18} | Priority: {self.priority} | Due: {self.due_date}"
