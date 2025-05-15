from datetime import datetime
import os

def validate_dates(start, deadline):
    return deadline >= start

def save_task_to_file(filename, title, category, priority, start, deadline, status):
    if not filename.endswith(".txt"):
        filename += ".txt"

    created_at = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    task_line = f"{title}|{category}|{priority}|{start.strftime('%d.%m.%Y')}|{deadline.strftime('%d.%m.%Y')}|{status}|{created_at}\n"

    with open(filename, "a", encoding="utf-8") as f:
        f.write(task_line)

    return f"Aufgabe '{title}' gespeichert."
