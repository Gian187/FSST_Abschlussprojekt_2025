'''
ABSCHLUSSPROJEKT FSST 4BHEL 2024/25
-----------------------------------------
Aufgabenplaner mit Zugriff über Sockets
-----------------------------------------
Briola Gianluca         Alimgeriev Muslim
'''

### LIBRARIES
import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import datetime
import os

### FILES
from addtask import save_task_to_file, validate_dates

# Funktion zum Speichern der Aufgabe
def aufgabe_speichern():
    try:
        title = nameentry.get().strip()
        category = beschreibungentry.get().strip() or "Allgemein"
        priority = prioauswahl.get()
        status = statusauswahl.get()
        start = datetime.strptime(startdatum.get(), "%d.%m.%Y")
        deadline = datetime.strptime(deadlinedatum.get(), "%d.%m.%Y")

        if not validate_dates(start, deadline):
            messagebox.showerror("Fehler", "❌ Deadline darf nicht vor dem Startdatum liegen.")
            return

        result = save_task_to_file("tasks.txt", title, category, priority, start, deadline, status)
        messagebox.showinfo("Gespeichert", f"✅ {result}")
        lade_aufgaben()
    except ValueError:
        messagebox.showerror("Fehler", "❌ Ungültiges Datumsformat. Bitte TT.MM.JJJJ eingeben.")
    except Exception as e:
        messagebox.showerror("Fehler", f"❌ Fehler beim Speichern: {str(e)}")


# Funktion zum Laden der Aufgaben
def lade_aufgaben():
    aufgaben_frame.destroy()
    erstelle_aufgabenliste()

# Funktion zum Löschen einer Aufgabe
def aufgabe_loeschen(index):
    with open("tasks.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
    if 0 <= index < len(lines):
        del lines[index]
    with open("tasks.txt", "w", encoding="utf-8") as file:
        file.writelines(lines)
    lade_aufgaben()

# Funktion zur Anzeige der Aufgabenliste
def erstelle_aufgabenliste():
    global aufgaben_frame
    aufgaben_frame = tk.Frame(tkFenster)
    aufgaben_frame.pack(pady=10)

    titel = tk.Label(aufgaben_frame, text="📋 Aufgabenliste:", font=("Helvetica", 16, 'bold'))
    titel.grid(row=0, column=0, columnspan=3, sticky='w', pady=(10, 10))

    if not os.path.exists("tasks.txt"):
        return

    with open("tasks.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    for index, line in enumerate(lines):
        teile = line.strip().split('|')
        if len(teile) < 7:
            continue

        info = f"📝 {teile[0]} | Kategorie: {teile[1]} | Priorität: {teile[2]} | Start: {teile[3]} | Deadline: {teile[4]} | Status: {teile[5]} | Erstellt am: {teile[6]}"
        label = tk.Label(aufgaben_frame, text=info, font=("Helvetica", 11), anchor='w', justify='left', wraplength=800)
        label.grid(row=index+1, column=0, sticky='w', pady=2, padx=10)

        delete_button = tk.Button(aufgaben_frame, text="❌ Löschen", font=("Helvetica", 10), bg="red", fg="white",
                                  command=lambda i=index: aufgabe_loeschen(i))
        delete_button.grid(row=index+1, column=1, padx=5)


### GUI Aufbau

tkFenster = tk.Tk()
tkFenster.geometry("1000x800")
tkFenster.title('Aufgabenplaner')

titel = tk.Label(tkFenster, text="Aufgabenplaner", font=("Helvetica", 24))
titel.pack(pady=20)

untertitel = tk.Label(tkFenster, text="Aufgabe hinzufügen:", font=("Helvetica", 15))
untertitel.pack(pady=10)

formular_frame = tk.Frame(tkFenster)
formular_frame.pack(pady=10)

# Name
namelabel = tk.Label(formular_frame, text="Name:", font=("Helvetica", 12), anchor='w', width=15)
namelabel.grid(row=0, column=0, padx=5, pady=5, sticky='w')
nameentry = tk.Entry(formular_frame, font=("Helvetica", 12), width=40)
nameentry.grid(row=0, column=1, padx=5, pady=5)

# Beschreibung
beschreibunglabel = tk.Label(formular_frame, text="Beschreibung:", font=("Helvetica", 12), anchor='w', width=15)
beschreibunglabel.grid(row=1, column=0, padx=5, pady=5, sticky='w')
beschreibungentry = tk.Entry(formular_frame, font=("Helvetica", 12), width=40)
beschreibungentry.grid(row=1, column=1, padx=5, pady=5)

# Priorität
priolabel = tk.Label(formular_frame, text="Priorität:", font=("Helvetica", 12), anchor='w', width=15)
priolabel.grid(row=2, column=0, padx=5, pady=5, sticky='w')
prioauswahl = tk.StringVar()
prioauswahl.set("Bitte wählen")
priodropdown = tk.OptionMenu(formular_frame, prioauswahl, "Hoch", "Mittel", "Niedrig")
priodropdown.config(font=("Helvetica", 12), width=37)
priodropdown.grid(row=2, column=1, padx=5, pady=5)

# Startdatum
startlabel = tk.Label(formular_frame, text="Startdatum:", font=("Helvetica", 12), anchor='w', width=15)
startlabel.grid(row=3, column=0, padx=5, pady=5, sticky='w')
startdatum = DateEntry(formular_frame, font=("Helvetica", 12), width=37, date_pattern="dd.mm.yyyy")
startdatum.grid(row=3, column=1, padx=5, pady=5)

# Deadline
deadlinelabel = tk.Label(formular_frame, text="Deadline:", font=("Helvetica", 12), anchor='w', width=15)
deadlinelabel.grid(row=4, column=0, padx=5, pady=5, sticky='w')
deadlinedatum = DateEntry(formular_frame, font=("Helvetica", 12), width=37, date_pattern="dd.mm.yyyy")
deadlinedatum.grid(row=4, column=1, padx=5, pady=5)

# Status
statuslabel = tk.Label(formular_frame, text="Status:", font=("Helvetica", 12), anchor='w', width=15)
statuslabel.grid(row=5, column=0, padx=5, pady=5, sticky='w')
statusauswahl = tk.StringVar()
statusauswahl.set("Offen")
statusdropdown = tk.OptionMenu(formular_frame, statusauswahl, "Offen", "In Bearbeitung", "Erledigt")
statusdropdown.config(font=("Helvetica", 12), width=37)
statusdropdown.grid(row=5, column=1, padx=5, pady=5)

# Speichern
speicher_button = tk.Button(tkFenster, text="📝 Aufgabe speichern", font=("Helvetica", 14), bg="green", fg="white", command=aufgabe_speichern)
speicher_button.pack(pady=20)

erstelle_aufgabenliste()
tkFenster.mainloop()
