"""
QuizEngine Service Controller
"""

import json
import random
from pathlib import Path
from models.question import Question

class QuizEngine:
    def __init__(self, json_path="data/questions.json"):
        self.json_path = Path(json_path)
        self.json_path.parent.mkdir(exist_ok=True)
        self.questions = self.load()
        self.results = []

    def load(self):
        if not self.json_path.exists():
            return []
        try:
            with open(self.json_path, "r", encoding="utf-8") as f:
                return [Question.from_dict(d) for d in json.load(f)]
        except Exception:
            return []

    def save(self):
        with open(self.json_path, "w", encoding="utf-8") as f:
            json.dump([q.to_dict() for q in self.questions], f, indent=4)

    def add_question(self, q_id, prompt, choices, correct_idx, category):
        self.questions.append(Question(q_id, prompt, choices, correct_idx, category))
        self.save()
        return True

    def run_quiz(self):
        if not self.questions:
            return 0, 0
        shuffled = self.questions.copy()
        random.shuffle(shuffled)
        score = 0
        for i, q in enumerate(shuffled, 1):
            print(f"\nQ{i}: {q.prompt} ({q.category})")
            for idx, choice in enumerate(q.choices):
                print(f"  {idx}. {choice}")
            ans = input("Enter choice index (e.g., 0): ").strip()
            if ans.isdigit() and int(ans) == q.correct_index:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Incorrect. Correct choice was: {q.choices[q.correct_index]}")
        self.results.append((score, len(shuffled)))
        return score, len(shuffled)
