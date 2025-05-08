'''
Autor / Author: Muslim Alimgeriev

Code Beschreibung / Description:

Diese Funktion arbeitet mit der File-IO-Bibliothek in Python und ermöglicht das Erstellen und Verwalten eines Aufgabenplaners.
Der Benutzer kann Aufgaben mit Titel, Kategorie, Priorität, Startdatum, Deadline und Status erfassen.
Alle Aufgaben werden in einer .txt-Datei gespeichert, wobei das Format so strukturiert ist, dass eine geordnete Auslesung und Verwaltung der Aufgaben möglich ist.
Das Programm stellt sicher, dass das Startdatum nicht später als das Deadline-Datum ist. Der Benutzer kann den Status der Aufgaben später ändern.
Der Benutzer hat die Möglichkeit, eine neue Datei zu erstellen oder eine bestehende Datei auszuwählen.

Funktionen:
- Aufgaben mit Titel, Kategorie, Priorität, Startdatum, Deadline und Status erfassen
- Aufgaben in einer .txt-Datei speichern
- Plausibilitätsprüfung für Start- und Enddatum
- Status der Aufgaben ändern (Offen, In Bearbeitung, Erledigt)
- Auswahl der Datei zum Speichern der Aufgaben

This function uses Python's File I/O library to create and manage a task planner.
The user can enter tasks with a title, category, priority, start date, deadline, and status.
All tasks are stored in a .txt file, and the format is structured to allow for easy retrieval and management of tasks.
The program ensures that the start date is not later than the deadline date. The user can later change the status of the tasks.
The user has the option to create a new file or select an existing one for saving the tasks.

Features:
- Create tasks with title, category, priority, start date, deadline, and status
- Save tasks in a .txt file
- Validate start and deadline dates
- Change the status of tasks (Open, In Progress, Done)
- Option to select or create a file for saving tasks
'''

import os
from datetime import datetime

LANG = "en"

TEXTS = {
    "en": {
        "welcome": "Task Planner",
        "choose_lang": "Choose language / Sprache wählen:\n1. English\n2. Deutsch",
        "invalid": "Invalid input. Try again.",
        "menu": "\nWhat would you like to do?\n1. Create new task\n2. Change task status\n3. Exit",
        "filename": "Enter filename (new or existing): ",
        "title": "Title: ",
        "category": "Category: ",
        "priority": "\nChoose priority:",
        "start_date": "Start date (DD.MM.YYYY): ",
        "deadline": "Deadline (DD.MM.YYYY): ",
        "deadline_error": "Deadline cannot be before start date!",
        "status": "\nChoose status:",
        "saved": "Task saved to ",
        "change_status": "Change status",
        "task_title": "Enter title of task to update: ",
        "new_status": "Choose new status:",
        "not_found": "Task not found.",
        "status_updated": "Status updated.",
        "bye": "Goodbye!",
    },
    "de": {
        "welcome": "Aufgabenplaner",
        "choose_lang": "Choose language / Sprache wählen:\n1. English\n2. Deutsch",
        "invalid": "Ungültige Eingabe. Bitte erneut versuchen.",
        "menu": "\nWas möchtest du tun?\n1. Neue Aufgabe erstellen\n2. Status ändern\n3. Beenden",
        "filename": "Dateiname eingeben (neu oder vorhanden): ",
        "title": "Titel: ",
        "category": "Kategorie: ",
        "priority": "\nPriorität wählen:",
        "start_date": "Startdatum (TT.MM.JJJJ): ",
        "deadline": "Deadline (TT.MM.JJJJ): ",
        "deadline_error": "Deadline darf nicht vor Startdatum liegen!",
        "status": "\nStatus wählen:",
        "saved": "Aufgabe gespeichert in ",
        "change_status": "Status ändern",
        "task_title": "Titel der Aufgabe zum Ändern: ",
        "new_status": "Neuer Status:",
        "not_found": "Aufgabe nicht gefunden.",
        "status_updated": "Status aktualisiert.",
        "bye": "Auf Wiedersehen!",
    },
}

PRIORITIES = ["High", "Medium", "Low"]
STATUSES = ["Open", "In Progress", "Done"]

def translate(text_key):
    return TEXTS[LANG][text_key]

def choose_option(prompt, options):
    print(prompt)
    for idx, option in enumerate(options, 1):
        print(f"{idx}. {option}")
    while True:
        try:
            choice = int(input("➤ "))
            if 1 <= choice <= len(options):
                return options[choice - 1]
        except:
            pass
        print(translate("invalid"))

def get_date(prompt):
    while True:
        value = input(prompt).strip()
        if not value:
            return None
        try:
            return datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            print(translate("invalid"))

def create_task():
    filename = input(translate("filename")).strip()
    if not filename.endswith(".txt"):
        filename += ".txt"

    title = input(translate("title")).strip() or "No title"
    category = input(translate("category")).strip() or "General"
    priority = choose_option(translate("priority"), PRIORITIES)
    start = get_date(translate("start_date"))
    deadline = get_date(translate("deadline"))

    while deadline and start and deadline < start:
        print(translate("deadline_error"))
        deadline = get_date(translate("deadline"))

    status = choose_option(translate("status"), STATUSES)

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
    print(translate("saved") + f"'{filename}'")

def change_task_status():
    filename = input(translate("filename")).strip()
    if not os.path.exists(filename):
        print("File not found.")
        return

    title_search = input(translate("task_title")).strip().lower()
    new_status = choose_option(translate("new_status"), STATUSES)

    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    updated = False
    i = 0
    while i < len(lines):
        if lines[i].startswith("Title") and title_search in lines[i].lower():
            for j in range(7):
                if "Status" in lines[i + j]:
                    lines[i + j] = f"Status      : {new_status}\n"
                    updated = True
                    break
        i += 1

    if updated:
        with open(filename, "w", encoding="utf-8") as file:
            file.writelines(lines)
        print(translate("status_updated"))
    else:
        print(translate("not_found"))

def main():
    global LANG

    print("🌐 " + translate("choose_lang"))
    lang_input = input("➤ ")
    LANG = "en" if lang_input.strip() == "1" else "de"

    print(f"\n{translate('welcome')}")

    while True:
        print(translate("menu"))
        choice = input("➤ ").strip()
        if choice == "1":
            create_task()
        elif choice == "2":
            change_task_status()
        elif choice == "3":
            print(translate("bye"))
            break
        else:
            print(translate("invalid"))

# Start program
if __name__ == "__main__":
    main()
