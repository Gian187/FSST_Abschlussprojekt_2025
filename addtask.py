import os
from datetime import datetime

PRIORITIES = ["High", "Medium", "Low"]
STATUSES = ["Open", "In Progress", "Done"]

def validate_dates(start, deadline):
    if start and deadline and deadline < start:
        return False
    return True

def save_task_to_file(filename, title, category, priority, start, deadline, status):
    if not filename.endswith(".txt"):
        filename += ".txt"

    task = (
        f"==============================\n"
        f"Title       : {title}\n"
        f"Category    : {category}\n"
        f"Priority    : {priority}\n"
        f"Start Date  : {start.strftime('%d.%m.%Y') if start else 'Not set'}\n"
        f"Deadline    : {deadline.strftime('%d.%m.%Y') if deadline else 'Not set'}\n"
        f"Status      : {status}\n"
        f"Created At  : {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}\n"
        f"==============================\n\n"
    )

    with open(filename, "a", encoding="utf-8") as f:
        f.write(task)
    return f"Task saved to '{filename}'"

def update_task_status(filename, task_title, new_status):
    if not os.path.exists(filename):
        return "File not found."

    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    updated = False
    i = 0
    while i < len(lines):
        if lines[i].startswith("Title") and task_title.lower() in lines[i].lower():
            for j in range(7):
                if "Status" in lines[i + j]:
                    lines[i + j] = f"Status      : {new_status}\n"
                    updated = True
                    break
        i += 1

    if updated:
        with open(filename, "w", encoding="utf-8") as file:
            file.writelines(lines)
        return "Status updated."
    else:
        return "Task not found."
