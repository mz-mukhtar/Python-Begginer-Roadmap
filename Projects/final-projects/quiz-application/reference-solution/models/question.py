"""
Question Domain Model
"""

class Question:
    def __init__(self, q_id, prompt, choices, correct_index, category):
        self.q_id = q_id
        self.prompt = prompt
        self.choices = choices
        self.correct_index = int(correct_index)
        self.category = category

    def to_dict(self):
        return {
            "q_id": self.q_id,
            "prompt": self.prompt,
            "choices": self.choices,
            "correct_index": self.correct_index,
            "category": self.category
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["q_id"], data["prompt"], data["choices"], data["correct_index"], data["category"])
