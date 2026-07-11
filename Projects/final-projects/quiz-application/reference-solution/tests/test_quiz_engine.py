"""
Automated Unit Tests for Quiz Engine
"""

import unittest
from pathlib import Path
from services.quiz_engine import QuizEngine

class TestQuizEngine(unittest.TestCase):
    def setUp(self):
        self.test_json = Path("data/test_quiz.json")
        if self.test_json.exists():
            self.test_json.unlink()
        self.engine = QuizEngine(self.test_json)

    def tearDown(self):
        if self.test_json.exists():
            self.test_json.unlink()

    def test_add_question(self):
        self.engine.add_question("Q-100", "2+2?", ["3", "4", "5"], 1, "Math")
        self.assertEqual(len(self.engine.questions), 1)

if __name__ == "__main__":
    unittest.main()
