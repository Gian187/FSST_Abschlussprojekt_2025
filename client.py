import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import datetime
import socket
import json

SERVER_IP = '127.0.0.1'
SERVER_PORT = 5000

def send_request(data):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((SERVER_IP, SERVER_PORT))
            sock.sendall(json.dumps(data).encode('utf-8'))
            response = sock.recv(8192).decode('utf-8')
            return json.loads(response)
    except Exception as e:
        return {"error": str(e)}

def aufgabe_speichern():
    try:
        title = nameentry.get().strip()
        category = beschreibungentry.get().strip() or "Allgemein"
        priority = prioauswahl.get()
        status = statusauswahl.get()
        start = datetime.strptime(startdatum.get(), "%d.%m.%Y")
        deadline = datetime.strptime(deadlinedatum.get(), "%d.%m.%Y")

        if deadline < start:
            messagebox.showerror("Fehler", "Deadline darf nicht vor dem Startdatum liegen.")
            return

        request = {
            "action": "add",
            "title": title,
            "category": category,
            "priority": priority,
            "start": start.strftime("%d.%m.%Y"),
            "deadline": deadline.strftime("%d.%m.%Y"),
            "status": status
        }

        response = send_request(request)
        if "success" in response:
            messagebox.showinfo("Erfolg", response["success"])
        else:
            messagebox.showerror("Fehler", response.get("error", "Unbekannter Fehler"))
        lade_aufgaben()
    except Exception as e:
        messagebox.showerror("Fehler", str(e))

def aufgabe_loeschen(index):
    send_request({"action": "delete", "index": index})
    lade_aufgaben()

def status_wechseln(index):
    send_request({"action": "toggle_status", "index": index})
    lade_aufgaben()

def lade_aufgaben():
    global aufgaben_frame
    aufgaben_frame.destroy()
    erstelle_aufgabenliste()

def erstelle_aufgabenliste():
    global aufgaben_frame
    aufgaben_frame = tk.Frame(tkFenster)
    aufgaben_frame.pack(pady=10)

    titel = tk.Label(aufgaben_frame, text="Aufgabenliste:", font=("Helvetica", 16, 'bold'))
    titel.grid(row=0, column=0, columnspan=3, sticky='w', pady=(10, 10))

    response = send_request({"action": "get"})

    if "error" in response:
        messagebox.showerror("Fehler", response["error"])
        return

    tasks = response.get("tasks", [])

    for index, line in enumerate(tasks):
        teile = line.strip().split('|')
        if len(teile) < 7:
            continue

        info = f"{teile[0]} | Kategorie: {teile[1]} | Priorität: {teile[2]} | Start: {teile[3]} | Deadline: {teile[4]} | Status: {teile[5]} | Erstellt am: {teile[6]}"
        label = tk.Label(aufgaben_frame, text=info, font=("Helvetica", 11), anchor='w', justify='left', wraplength=800)
        label.grid(row=index+1, column=0, sticky='w', pady=2, padx=10)

        delete_button = tk.Button(aufgaben_frame, text="Löschen", font=("Helvetica", 10), bg="red", fg="white",
                                  command=lambda i=index: aufgabe_loeschen(i))
        delete_button.grid(row=index+1, column=1, padx=5)

        status_button = tk.Button(aufgaben_frame, text="Status ändern", font=("Helvetica", 10), bg="blue", fg="white",
                                  command=lambda i=index: status_wechseln(i))
        status_button.grid(row=index+1, column=2, padx=5)

# GUI Setup
tkFenster = tk.Tk()
tkFenster.geometry("1000x800")
tkFenster.title('Aufgabenplaner (Client)')

titel = tk.Label(tkFenster, text="Aufgabenplaner", font=("Helvetica", 24))
titel.pack(pady=20)

untertitel = tk.Label(tkFenster, text="Aufgabe hinzufügen:", font=("Helvetica", 15))
untertitel.pack(pady=10)

formular_frame = tk.Frame(tkFenster)
formular_frame.pack(pady=10)

namelabel = tk.Label(formular_frame, text="Name:", font=("Helvetica", 12), anchor='w', width=15)
namelabel.grid(row=0, column=0, padx=5, pady=5, sticky='w')
nameentry = tk.Entry(formular_frame, font=("Helvetica", 12), width=40)
nameentry.grid(row=0, column=1, padx=5, pady=5)

beschreibunglabel = tk.Label(formular_frame, text="Beschreibung:", font=("Helvetica", 12), anchor='w', width=15)
beschreibunglabel.grid(row=1, column=0, padx=5, pady=5, sticky='w')
beschreibungentry = tk.Entry(formular_frame, font=("Helvetica", 12), width=40)
beschreibungentry.grid(row=1, column=1, padx=5, pady=5)

priolabel = tk.Label(formular_frame, text="Priorität:", font=("Helvetica", 12), anchor='w', width=15)
priolabel.grid(row=2, column=0, padx=5, pady=5, sticky='w')
prioauswahl = tk.StringVar()
prioauswahl.set("Bitte wählen")
priodropdown = tk.OptionMenu(formular_frame, prioauswahl, "Hoch", "Mittel", "Niedrig")
priodropdown.config(font=("Helvetica", 12), width=37)
priodropdown.grid(row=2, column=1, padx=5, pady=5)

startlabel = tk.Label(formular_frame, text="Startdatum:", font=("Helvetica", 12), anchor='w', width=15)
startlabel.grid(row=3, column=0, padx=5, pady=5, sticky='w')
startdatum = DateEntry(formular_frame, font=("Helvetica", 12), width=37, date_pattern="dd.mm.yyyy")
startdatum.grid(row=3, column=1, padx=5, pady=5)

deadlinelabel = tk.Label(formular_frame, text="Deadline:", font=("Helvetica", 12), anchor='w', width=15)
deadlinelabel.grid(row=4, column=0, padx=5, pady=5, sticky='w')
deadlinedatum = DateEntry(formular_frame, font=("Helvetica", 12), width=37, date_pattern="dd.mm.yyyy")
deadlinedatum.grid(row=4, column=1, padx=5, pady=5)

statuslabel = tk.Label(formular_frame, text="Status:", font=("Helvetica", 12), anchor='w', width=15)
statuslabel.grid(row=5, column=0, padx=5, pady=5, sticky='w')
statusauswahl = tk.StringVar()
statusauswahl.set("Offen")
statusdropdown = tk.OptionMenu(formular_frame, statusauswahl, "Offen", "In Bearbeitung", "Erledigt")
statusdropdown.config(font=("Helvetica", 12), width=37)
statusdropdown.grid(row=5, column=1, padx=5, pady=5)

speicher_button = tk.Button(tkFenster, text="Aufgabe speichern", font=("Helvetica", 14), bg="green", fg="white", command=aufgabe_speichern)
speicher_button.pack(pady=20)

erstelle_aufgabenliste()

tkFenster.mainloop()
