"""
Automated Unit Tests for To-Do List Manager
"""

import unittest
from pathlib import Path
from services.task_manager import TaskManager

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.test_json = Path("data/test_tasks.json")
        if self.test_json.exists():
            self.test_json.unlink()
        self.manager = TaskManager(self.test_json)

    def tearDown(self):
        if self.test_json.exists():
            self.test_json.unlink()

    def test_complete_task(self):
        self.manager.add_task("TASK-100", "Study", "Read chapter", "2026-07-12", "High")
        self.assertTrue(self.manager.mark_complete("TASK-100"))
        self.assertTrue(self.manager.tasks[0].completed)

if __name__ == "__main__":
    unittest.main()
