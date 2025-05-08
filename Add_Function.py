'''
Autor / Author: Muslim Alimgeriev

Code Beschreibung / Description:

Diese Funktion arbeitet mit der File-IO-Bibliothek in Python und ist in eine grafische Benutzeroberfläche (GUI) integriert.
Über Schaltflächen (Buttons) in der GUI können Aufgaben hinzugefügt werden. Jede Aufgabe wird im .txt-Dateiformat gespeichert,
wobei ein strukturiertes Format verwendet wird, das eine spätere geordnete Auslesung ermöglicht. In der GUI werden alle gespeicherten
Aufgaben in einer Liste angezeigt – sortiert nach ihrer Priorität.

This function uses Python’s File I/O to manage tasks within a graphical user interface (GUI). Tasks can be added via buttons in the GUI,
and each task is saved in a structured format in a .txt file. This format ensures that tasks can later be read and displayed in an organized
way. All saved tasks are shown in a list within the GUI, sorted by priority.
'''

import os
from datetime import datetime

LANG = "en"

TEXTS = {
    "en": {
        "welcome": "📋 Task Planner",
        "choose_lang": "Choose language / Sprache wählen:\n1. English\n2. Deutsch",
        "invalid": "❌ Invalid input. Try again.",
        "menu": "\nWhat would you like to do?\n1. Create new task\n2. Change task status\n3. Exit",
        "filename": "Enter filename (new or existing): ",
        "title": "📌 Title: ",
        "category": "📂 Category: ",
        "priority": "\n⭐ Choose priority:",
        "start_date": "📅 Start date (DD.MM.YYYY): ",
        "deadline": "⏰ Deadline (DD.MM.YYYY): ",
        "deadline_error": "❌ Deadline cannot be before start date!",
        "status": "\n📌 Choose status:",
        "saved": "✅ Task saved to ",
        "change_status": "🔄 Change status",
        "task_title": "Enter title of task to update: ",
        "new_status": "✅ Choose new status:",
        "not_found": "❌ Task not found.",
        "status_updated": "✅ Status updated.",
        "bye": "👋 Goodbye!",
    },
    "de": {
        "welcome": "📋 Aufgabenplaner",
        "choose_lang": "Choose language / Sprache wählen:\n1. English\n2. Deutsch",
        "invalid": "❌ Ungültige Eingabe. Bitte erneut versuchen.",
        "menu": "\nWas möchtest du tun?\n1. Neue Aufgabe erstellen\n2. Status ändern\n3. Beenden",
        "filename": "Dateiname eingeben (neu oder vorhanden): ",
        "title": "📌 Titel: ",
        "category": "📂 Kategorie: ",
        "priority": "\n⭐ Priorität wählen:",
        "start_date": "📅 Startdatum (TT.MM.JJJJ): ",
        "deadline": "⏰ Deadline (TT.MM.JJJJ): ",
        "deadline_error": "❌ Deadline darf nicht vor Startdatum liegen!",
        "status": "\n📌 Status wählen:",
        "saved": "✅ Aufgabe gespeichert in ",
        "change_status": "🔄 Status ändern",
        "task_title": "Titel der Aufgabe zum Ändern: ",
        "new_status": "✅ Neuer Status:",
        "not_found": "❌ Aufgabe nicht gefunden.",
        "status_updated": "✅ Status aktualisiert.",
        "bye": "👋 Auf Wiedersehen!",
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
        print("❌ File not found.")
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
