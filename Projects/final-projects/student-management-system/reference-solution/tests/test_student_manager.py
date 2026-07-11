"""
Automated Unit Tests for Student Management System Capstone
"""

import unittest
from pathlib import Path
from services.student_manager import StudentManager

class TestStudentManagerReference(unittest.TestCase):
    def setUp(self):
        self.test_json = Path("data/test_students.json")
        self.test_csv = Path("data/test_students.csv")
        if self.test_json.exists():
            self.test_json.unlink()
        if self.test_csv.exists():
            self.test_csv.unlink()
        self.manager = StudentManager(self.test_json, self.test_csv)

    def tearDown(self):
        if self.test_json.exists():
            self.test_json.unlink()
        if self.test_csv.exists():
            self.test_csv.unlink()

    def test_add_and_search(self):
        ok, _ = self.manager.add_student("STU-100", "Sara", 20, "CS", "sara@example.com", ["Python"])
        self.assertTrue(ok)
        matches = self.manager.search_student("Sara")
        self.assertEqual(len(matches), 1)

    def test_update_and_delete(self):
        self.manager.add_student("STU-101", "Abel", 21, "SE", "abel@example.com", [])
        self.assertTrue(self.manager.update_student("STU-101", "CE", "new@example.com"))
        self.assertTrue(self.manager.delete_student("STU-101"))

if __name__ == "__main__":
    unittest.main()
