"""
Reference Entrypoint for To-Do List Manager Capstone
"""

from services.task_manager import TaskManager

def main():
    manager = TaskManager()

    while True:
        print("")
        print("========================================")
        print("      TO-DO LIST MANAGER CAPSTONE       ")
        print("========================================")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Filter Tasks (Completed/Pending)")
        print("4. Mark Task Complete")
        print("5. Delete Task")
        print("6. Exit")
        print("========================================")

        choice = input("Enter choice (1-6): ").strip()

        if choice == "1":
            tid = input("Enter Task ID (e.g., TASK-002): ").strip()
            title = input("Enter Task Title: ").strip()
            desc = input("Enter Description: ").strip()
            due = input("Enter Due Date (YYYY-MM-DD): ").strip()
            prio = input("Enter Priority (High/Medium/Low): ").strip()
            ok, msg = manager.add_task(tid, title, desc, due, prio)
            print(f"{'✅' if ok else '❌'} {msg}")

        elif choice == "2":
            for t in manager.tasks:
                print(t)

        elif choice == "3":
            status_input = input("Show completed tasks? (y/n): ").strip().lower()
            filtered = manager.filter_by_status(status_input == "y")
            for t in filtered:
                print(t)

        elif choice == "4":
            tid = input("Enter Task ID to mark complete: ").strip()
            print("✅ Marked complete." if manager.mark_complete(tid) else "❌ Task ID not found.")

        elif choice == "5":
            tid = input("Enter Task ID to delete: ").strip()
            print("✅ Deleted." if manager.delete_task(tid) else "❌ Task ID not found.")

        elif choice == "6":
            print("Exiting To-Do List Manager. Goodbye!")
            break

        else:
            print("Invalid selection.")

if __name__ == "__main__":
    main()
