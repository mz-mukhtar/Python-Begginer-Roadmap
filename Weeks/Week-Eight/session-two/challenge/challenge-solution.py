"""
Challenge Solution: Professional CLI Student Dashboard
Week Eight — Session Two
"""

class StudentUI:
    @staticmethod
    def show_banner():
        print("\n" + "=" * 50)
        print("    STUDENT MANAGEMENT SYSTEM - DASHBOARD    ")
        print("=" * 50)

    @staticmethod
    def render_table(students):
        print(f"{'ID':<6} | {'NAME':<18} | {'MAJOR':<15}")
        print("-" * 50)
        for s in students:
            print(f"{s['id']:<6} | {s['name']:<18} | {s['major']:<15}")

StudentUI.show_banner()
StudentUI.render_table([{"id": 101, "name": "Abel Tadesse", "major": "CS"}])
