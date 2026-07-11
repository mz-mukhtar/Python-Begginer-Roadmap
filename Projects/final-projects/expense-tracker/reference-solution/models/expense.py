"""
Expense Domain Model
"""

class Expense:
    def __init__(self, expense_id, description, amount, category, date_str):
        self.expense_id = expense_id
        self.description = description
        self.amount = float(amount)
        self.category = category
        self.date_str = date_str

    def to_dict(self):
        return {
            "expense_id": self.expense_id,
            "description": self.description,
            "amount": self.amount,
            "category": self.category,
            "date_str": self.date_str
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["expense_id"], data["description"], data["amount"], data["category"], data["date_str"])

    def __str__(self):
        return f"[{self.expense_id}] {self.date_str} | {self.description:<20} | {self.category:<12} | ${self.amount:.2f}"
