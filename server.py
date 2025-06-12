import socket
import threading
import json
from datetime import datetime
import os

HOST = '127.0.0.1'
PORT = 5000
TASK_FILE = "tasks.txt"

def handle_client(conn, addr):
    with conn:
        print(f"Client verbunden: {addr}")
        while True:
            try:
                data = conn.recv(4096).decode('utf-8')
                if not data:
                    break
                request = json.loads(data)
                response = process_request(request)
                conn.send(json.dumps(response).encode('utf-8'))
            except Exception as e:
                conn.send(json.dumps({"error": str(e)}).encode('utf-8'))
                break

def process_request(req):
    action = req.get("action")

    if action == "add":
        return add_task(req)
    elif action == "get":
        return get_tasks()
    elif action == "delete":
        return delete_task(req.get("index"))
    elif action == "toggle_status":
        return toggle_status(req.get("index"))
    else:
        return {"error": "Unbekannte Aktion"}

def add_task(data):
    # Neue Aufgabe als Textzeile abspeichern
    title = data["title"]
    category = data.get("category", "Allgemein")
    priority = data["priority"]
    start = data["start"]
    deadline = data["deadline"]
    status = data["status"]
    created_at = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    line = f"{title}|{category}|{priority}|{start}|{deadline}|{status}|{created_at}\n"
    with open(TASK_FILE, "a", encoding="utf-8") as f:
        f.write(line)
    return {"success": f"Aufgabe '{title}' gespeichert."}

def get_tasks():
    if not os.path.exists(TASK_FILE):
        return {"tasks": []}
    with open(TASK_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return {"tasks": lines}

def delete_task(index):
    with open(TASK_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
    try:
        index = int(index)
        if 0 <= index < len(lines):
            del lines[index]
            with open(TASK_FILE, "w", encoding="utf-8") as f:
                f.writelines(lines)
            return {"success": "Aufgabe gelöscht"}
    except:
        return {"error": "Ungültiger Index"}
    return {"error": "Fehler beim Löschen"}

def toggle_status(index):
    # Status rotiert zwischen Offen → In Bearbeitung → Erledigt
    with open(TASK_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
    try:
        index = int(index)
        teile = lines[index].strip().split('|')
        status_map = {"Offen": "In Bearbeitung", "In Bearbeitung": "Erledigt", "Erledigt": "Offen"}
        teile[5] = status_map.get(teile[5], "Offen")
        lines[index] = '|'.join(teile) + '\n'
        with open(TASK_FILE, "w", encoding="utf-8") as f:
            f.writelines(lines)
        return {"success": "Status geändert"}
    except:
        return {"error": "Fehler beim Statuswechsel"}

def main():
    print(f"Server läuft auf {HOST}:{PORT}")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        while True:
            conn, addr = s.accept()
            threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    main()
