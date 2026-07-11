"""
Automated Unit Tests for Expense Tracker
"""

import unittest
from pathlib import Path
from services.expense_manager import ExpenseManager

class TestExpenseManager(unittest.TestCase):
    def setUp(self):
        self.test_json = Path("data/test_exp.json")
        if self.test_json.exists():
            self.test_json.unlink()
        self.manager = ExpenseManager(self.test_json)

    def tearDown(self):
        if self.test_json.exists():
            self.test_json.unlink()

    def test_summary(self):
        self.manager.add_expense("EXP-100", "Book", 50.0, "Edu", "2026-07-11")
        self.manager.add_expense("EXP-101", "Lunch", 15.0, "Food", "2026-07-11")
        total, by_cat = self.manager.calculate_summary()
        self.assertEqual(total, 65.0)
        self.assertEqual(by_cat["Edu"], 50.0)

if __name__ == "__main__":
    unittest.main()
