"""
TaskManager Service Controller
"""

import json
from pathlib import Path
from models.task import Task

class TaskManager:
    def __init__(self, json_path="data/tasks.json"):
        self.json_path = Path(json_path)
        self.json_path.parent.mkdir(exist_ok=True)
        self.tasks = self.load()

    def load(self):
        if not self.json_path.exists():
            return []
        try:
            with open(self.json_path, "r", encoding="utf-8") as f:
                return [Task.from_dict(d) for d in json.load(f)]
        except Exception:
            return []

    def save(self):
        with open(self.json_path, "w", encoding="utf-8") as f:
            json.dump([t.to_dict() for t in self.tasks], f, indent=4)

    def add_task(self, tid, title, desc, due, priority):
        if any(t.task_id == tid for t in self.tasks):
            return False, "Task ID already exists."
        self.tasks.append(Task(tid, title, desc, due, priority))
        self.save()
        return True, "Task added successfully."

    def mark_complete(self, tid):
        for t in self.tasks:
            if t.task_id == tid:
                t.completed = True
                self.save()
                return True
        return False

    def filter_by_status(self, completed_flag):
        return [t for t in self.tasks if t.completed == completed_flag]

    def delete_task(self, tid):
        for i, t in enumerate(self.tasks):
            if t.task_id == tid:
                del self.tasks[i]
                self.save()
                return True
        return False
