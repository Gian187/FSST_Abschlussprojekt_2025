'''
Graphical User Interface

Briola
'''

import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import datetime

# Fenster erstellen
tkFenster = tk.Tk()
tkFenster.geometry("1000x800")
tkFenster.title('Aufgabenplaner')

# ------------------ Überschrift ------------------
titel = tk.Label(tkFenster, text="Aufgabenplaner", font=("Helvetica", 24))
titel.pack(pady=20)

untertitel = tk.Label(tkFenster, text="Aufgabe hinzufügen:", font=("Helvetica", 15))
untertitel.pack(pady=10)



# ------------------ Eingabeformular ------------------
formular_frame = tk.Frame(tkFenster)
formular_frame.pack(pady=10)

# Zeile: Name
namelabel = tk.Label(formular_frame, text="Name:", font=("Helvetica", 12), anchor='w', width=15)
namelabel.grid(row=0, column=0, padx=5, pady=5, sticky='w')
nameentry = tk.Entry(formular_frame, font=("Helvetica", 12), width=40)
nameentry.grid(row=0, column=1, padx=5, pady=5)

# Zeile: Beschreibung
beschreibunglabel = tk.Label(formular_frame, text="Beschreibung:", font=("Helvetica", 12), anchor='w', width=15)
beschreibunglabel.grid(row=1, column=0, padx=5, pady=5, sticky='w')
beschreibungentry = tk.Entry(formular_frame, font=("Helvetica", 12), width=40)
beschreibungentry.grid(row=1, column=1, padx=5, pady=5)

# Zeile: Priorität
priolabel = tk.Label(formular_frame, text="Priorität:", font=("Helvetica", 12), anchor='w', width=15)
priolabel.grid(row=2, column=0, padx=5, pady=5, sticky='w')
prioauswahl = tk.StringVar()
prioauswahl.set("Bitte wählen")
priodropdown = tk.OptionMenu(formular_frame, prioauswahl, "Hoch", "Mittel", "Niedrig")
priodropdown.config(font=("Helvetica", 12), width=37)
priodropdown.grid(row=2, column=1, padx=5, pady=5)

# Zeile: Startdatum
startlabel = tk.Label(formular_frame, text="Startdatum:", font=("Helvetica", 12), anchor='w', width=15)
startlabel.grid(row=3, column=0, padx=5, pady=5, sticky='w')
startdatum = DateEntry(formular_frame, font=("Helvetica", 12), width=37, date_pattern="dd.mm.yyyy")
startdatum.grid(row=3, column=1, padx=5, pady=5)

# Zeile: Deadline
deadlinelabel = tk.Label(formular_frame, text="Deadline:", font=("Helvetica", 12), anchor='w', width=15)
deadlinelabel.grid(row=4, column=0, padx=5, pady=5, sticky='w')
deadlinedatum = DateEntry(formular_frame, font=("Helvetica", 12), width=37, date_pattern="dd.mm.yyyy")
deadlinedatum.grid(row=4, column=1, padx=5, pady=5)

# Zeile: Status
statuslabel = tk.Label(formular_frame, text="Status:", font=("Helvetica", 12), anchor='w', width=15)
statuslabel.grid(row=5, column=0, padx=5, pady=5, sticky='w')
statusauswahl = tk.StringVar()
statusauswahl.set("Offen")
statusdropdown = tk.OptionMenu(formular_frame, statusauswahl, "Offen", "In Bearbeitung", "Erledigt")
statusdropdown.config(font=("Helvetica", 12), width=37)
statusdropdown.grid(row=5, column=1, padx=5, pady=5)

# Zeile: Created At
createdlabel = tk.Label(formular_frame, text="Created At:", font=("Helvetica", 12), anchor='w', width=15)
createdlabel.grid(row=6, column=0, padx=5, pady=5, sticky='w')
created_value = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
createdentry = tk.Entry(formular_frame, font=("Helvetica", 12), width=40)
createdentry.insert(0, created_value)
createdentry.config(state='readonly')
createdentry.grid(row=6, column=1, padx=5, pady=5)




'''

# Zum abschauen

# Eingabefeld
eingabe_feld = tk.Entry(tkFenster, width=50, font=("Helvetica", 14))
eingabe_feld.pack(pady=10)

# Hinzufügen-Button
hinzufuegen_button = tk.Button(tkFenster, text="Aufgabe hinzufügen", font=("Helvetica", 14))
hinzufuegen_button.pack(pady=10)

# Aufgabenliste (Listbox)
aufgaben_liste = tk.Listbox(tkFenster, width=50, height=10, font=("Helvetica", 12))
aufgaben_liste.pack(pady=20)
'''


# Aktivierung des Fensters
tkFenster.mainloop()