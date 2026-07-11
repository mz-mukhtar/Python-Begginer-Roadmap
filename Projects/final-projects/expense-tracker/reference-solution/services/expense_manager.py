"""
ExpenseManager Service Controller
"""

import json
import csv
from pathlib import Path
from models.expense import Expense

class ExpenseManager:
    def __init__(self, json_path="data/expenses.json", csv_path="data/expenses.csv"):
        self.json_path = Path(json_path)
        self.csv_path = Path(csv_path)
        self.json_path.parent.mkdir(exist_ok=True)
        self.expenses = self.load()

    def load(self):
        if not self.json_path.exists():
            return []
        try:
            with open(self.json_path, "r", encoding="utf-8") as f:
                return [Expense.from_dict(d) for d in json.load(f)]
        except Exception:
            return []

    def save(self):
        with open(self.json_path, "w", encoding="utf-8") as f:
            json.dump([e.to_dict() for e in self.expenses], f, indent=4)

    def add_expense(self, eid, desc, amt, cat, date_str):
        if any(e.expense_id == eid for e in self.expenses):
            return False, "Expense ID already exists."
        self.expenses.append(Expense(eid, desc, amt, cat, date_str))
        self.save()
        return True, "Expense added successfully."

    def filter_by_category(self, cat):
        return [e for e in self.expenses if e.category.lower() == cat.lower()]

    def calculate_summary(self):
        total = sum(e.amount for e in self.expenses)
        by_cat = {}
        for e in self.expenses:
            by_cat[e.category] = by_cat.get(e.category, 0.0) + e.amount
        return total, by_cat

    def export_csv(self):
        with open(self.csv_path, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["Expense ID", "Date", "Description", "Category", "Amount"])
            for e in self.expenses:
                w.writerow([e.expense_id, e.date_str, e.description, e.category, e.amount])
        return self.csv_path
