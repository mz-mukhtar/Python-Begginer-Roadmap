"""
Automated Unit Tests for Student Model
"""

import unittest
from models.student import Student

class TestStudentModel(unittest.TestCase):
    def test_student_creation(self):
        s = Student("STU-100", "Abel", "CS")
        self.assertEqual(s.student_id, "STU-100")
        self.assertEqual(s.name, "Abel")
        self.assertEqual(s.major, "CS")

    def test_serialization(self):
        s = Student("STU-100", "Abel", "CS")
        data = s.to_dict()
        self.assertEqual(data["student_id"], "STU-100")
        s_restored = Student.from_dict(data)
        self.assertEqual(s_restored.name, "Abel")

if __name__ == "__main__":
    unittest.main()
