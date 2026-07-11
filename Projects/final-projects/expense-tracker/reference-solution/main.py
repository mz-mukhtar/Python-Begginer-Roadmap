"""
Reference Entrypoint for Expense Tracker Capstone
"""

from services.expense_manager import ExpenseManager

def main():
    manager = ExpenseManager()

    while True:
        print("")
        print("========================================")
        print("        EXPENSE TRACKER CAPSTONE        ")
        print("========================================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search Expenses")
        print("4. Filter by Category")
        print("5. Update Expense")
        print("6. Delete Expense")
        print("7. Display Summary")
        print("8. Export Report")
        print("9. Exit")
        print("========================================")

        choice = input("Enter choice (1-9): ").strip()

        if choice == "1":
            eid = input("Enter ID (e.g., EXP-002): ").strip()
            desc = input("Enter Description: ").strip()
            amt = float(input("Enter Amount ($): ").strip())
            cat = input("Enter Category (Education/Food/Transport): ").strip()
            date_s = input("Enter Date (YYYY-MM-DD): ").strip()
            ok, msg = manager.add_expense(eid, desc, amt, cat, date_s)
            print(f"{'✅' if ok else '❌'} {msg}")

        elif choice == "2":
            for e in manager.expenses:
                print(e)

        elif choice == "4":
            cat = input("Enter Category to filter: ").strip()
            for e in manager.filter_by_category(cat):
                print(e)

        elif choice == "7":
            total, by_cat = manager.calculate_summary()
            print(f"💰 Total Spending: ${total:.2f}")
            print("--- Breakdown by Category ---")
            for c, amt in by_cat.items():
                print(f"• {c}: ${amt:.2f}")

        elif choice == "8":
            print(f"✅ Exported report to {manager.export_csv()}")

        elif choice in ("3", "5", "6"):
            print("Feature implemented in manager service.")

        elif choice == "9":
            print("Exiting Expense Tracker. Goodbye!")
            break

        else:
            print("Invalid selection.")

if __name__ == "__main__":
    main()
