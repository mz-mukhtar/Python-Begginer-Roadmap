"""
Automated Unit Tests for StudentManager Controller
"""

import unittest
from pathlib import Path
from models.student import Student
from utilities.file_manager import StorageRepository
from services.student_manager import StudentManager

class TestStudentManager(unittest.TestCase):
    def setUp(self):
        self.test_file = Path("data/test_manager.json")
        if self.test_file.exists():
            self.test_file.unlink()
        self.repo = StorageRepository("data/test_manager.json")
        self.manager = StudentManager(self.repo)

    def tearDown(self):
        if self.test_file.exists():
            self.test_file.unlink()

    def test_add_and_duplicate(self):
        success, _ = self.manager.add_student("STU-999", "Sara", "EE")
        self.assertTrue(success)
        self.assertEqual(len(self.manager.get_all()), 1)

        dup_success, _ = self.manager.add_student("STU-999", "Duplicate", "EE")
        self.assertFalse(dup_success)

    def test_find_and_delete(self):
        self.manager.add_student("STU-101", "Mahi", "CS")
        found = self.manager.find_by_id("STU-101")
        self.assertIsNotNone(found)
        self.assertTrue(self.manager.delete_student("STU-101"))
        self.assertIsNone(self.manager.find_by_id("STU-101"))

if __name__ == "__main__":
    unittest.main()
