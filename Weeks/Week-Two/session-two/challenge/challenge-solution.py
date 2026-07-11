"""
Challenge Solution: Classroom Attendance List
Week Two — Session Two
"""

attendees = []
print("=== Attendance Register (Type 'q' to stop) ===")
while True:
    name = input("Enter student name: ").strip()
    if name.lower() == 'q':
        break
    if name:
        attendees.append(name)

attendees.sort()
print("")
print("=== Classroom Roster ===")
print("Total Attendees:", len(attendees))
for i, name in enumerate(attendees, 1):
    print(f"{i}. {name}")
