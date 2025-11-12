# deadline_tracker_input.py
from datetime import datetime

print("Assignment Deadline Tracker")
print("-" * 30)

assignments = []

# Input loop
while True:
    name = input("Assignment name (or 'done' to finish): ").strip()
    if name.lower() == 'done':
        break
    due = input("Due date (YYYY-MM-DD HH:MM): ").strip()
    assignments.append((name, due))

# Check and display
print("\nYour Deadlines:")
now = datetime.now()
for name, due in assignments:
    try:
        due_time = datetime.strptime(due, "%Y-%m-%d %H:%M")
        hours_left = (due_time - now).total_seconds() / 3600
        if hours_left < 0:
            print(f"MISSED: {name}")
        elif hours_left < 24:
            print(f"DUE SOON: {name} ({hours_left:.1f}h left)")
        else:
            print(f"{name} due {due}")
    except:
        print(f"Invalid date: {name} - {due}")