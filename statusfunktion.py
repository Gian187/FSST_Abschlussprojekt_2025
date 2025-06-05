        status_button = tk.Button(aufgaben_frame, text="Status ändern", font=("Helvetica", 10), bg="blue", fg="white",
                                  command=lambda i=index: status_wechseln(i))
        status_button.grid(row=index+1, column=2, padx=5)


def status_wechseln(index):
    with open("tasks.txt", "r") as file:
        lines = file.readlines()

    if 0 <= index < len(lines):
        teile = lines[index].strip().split('|')
        if len(teile) >= 7:
            aktueller_status = teile[5].strip()
            neue_status = {
                "Offen": "In Bearbeitung",
                "In Bearbeitung": "Erledigt",
                "Erledigt": "Offen"
            }
            teile[5] = neue_status.get(aktueller_status, "Offen")
            lines[index] = '|'.join(teile) + '\n'

            with open("tasks.txt", "w", encoding="utf-8") as file:
                file.writelines(lines)
            lade_aufgaben()