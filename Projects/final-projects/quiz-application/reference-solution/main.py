"""
Reference Entrypoint for Quiz Application Capstone
"""

from services.quiz_engine import QuizEngine

def main():
    engine = QuizEngine()

    while True:
        print("")
        print("========================================")
        print("        QUIZ APPLICATION CAPSTONE       ")
        print("========================================")
        print("1. Start Quiz")
        print("2. View Available Questions")
        print("3. View Previous Results")
        print("4. Add Question")
        print("5. Exit")
        print("========================================")

        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":
            score, total = engine.run_quiz()
            print(f"\n🏁 Final Score: {score} / {total}")

        elif choice == "2":
            for q in engine.questions:
                print(f"[{q.q_id}] {q.prompt} (Category: {q.category})")

        elif choice == "3":
            if not engine.results:
                print("No quiz attempts yet.")
            else:
                for idx, (s, t) in enumerate(engine.results, 1):
                    print(f"Attempt {idx}: {s} / {t}")

        elif choice == "4":
            qid = input("Enter Question ID: ").strip()
            prompt = input("Enter Question Prompt: ").strip()
            choices = [c.strip() for c in input("Enter 4 choices comma-separated: ").split(",")]
            correct_idx = int(input("Enter correct choice index (0 to 3): ").strip())
            cat = input("Enter Category: ").strip()
            engine.add_question(qid, prompt, choices, correct_idx, cat)
            print("✅ Question added successfully.")

        elif choice == "5":
            print("Exiting Quiz Application. Goodbye!")
            break

        else:
            print("Invalid selection.")

if __name__ == "__main__":
    main()
