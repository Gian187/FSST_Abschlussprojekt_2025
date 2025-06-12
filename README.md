# 📋 Aufgabenplaner über Sockets – Abschlussprojekt FSST 4BHEL 2024/25

## 🔧 Projektbeschreibung

Dies ist ein einfacher Aufgabenplaner mit Client-Server-Architektur über Sockets. Die Anwendung besteht aus zwei Teilen:

- **Server** (Python): Verwaltet Aufgaben, speichert sie in einer Datei und verarbeitet Anfragen vom Client.
- **Client** (Python mit Tkinter): Bietet eine grafische Benutzeroberfläche, um Aufgaben hinzuzufügen, zu löschen und deren Status zu ändern.

Das Projekt wurde im Rahmen des Abschlussprojekts der **4BHEL** an der **HTL** realisiert.

👥 Projektteam:\
**Briola Gianluca**\
**Alimgeriev Muslim**

---

## 📁 Projektstruktur

```bash
📆 projekt/
 ├│ 📄 server.py          # Server-Code zur Aufgabenverwaltung über Sockets
 ├│ 📄 client.py          # Tkinter-Client zur GUI-basierten Aufgabenplanung
 ├│ 📄 tasks.txt          # Lokale Datei, in der Aufgaben gespeichert werden
 └│ 📄 README.md          # Diese Projektbeschreibung
```

---

## 🚀 Funktionen

✅ Aufgaben erstellen mit:

- Titel
- Beschreibung (Kategorie)
- Priorität (Hoch, Mittel, Niedrig)
- Startdatum & Deadline
- Status (Offen, In Bearbeitung, Erledigt)

✅ Aufgaben abrufen und anzeigen\
✅ Aufgaben löschen\
✅ Aufgabenstatus zyklisch ändern\
✅ Daten lokal speichern (`tasks.txt`)\
✅ Kommunikation über Sockets mit JSON-Format

---

## ▶️ Voraussetzungen

- Python 3.7 oder neuer
- Folgende Python-Bibliotheken:
  - `tkinter` (Standard bei Python)
  - `tkcalendar`
  - `socket`
  - `threading`

Installation fehlender Module:

```bash
pip install tkcalendar
```

---

## 🧐 Nutzung

### 1. Starte den Server

```bash
python server.py
```

Der Server läuft standardmäßig auf `127.0.0.1:5000`.

---

### 2. Starte den Client

```bash
python client.py
```

Es öffnet sich ein GUI-Fenster zum Planen deiner Aufgaben.

---

## 💾 Speicherung

Aufgaben werden lokal in einer Textdatei (`tasks.txt`) im folgenden Format gespeichert:

```text
Titel|Kategorie|Priorität|Startdatum|Deadline|Status|Erstellt am
```

Beispiel:

```text
Mathe lernen|Schule|Hoch|12.06.2025|15.06.2025|Offen|12.06.2025 10:15:32
```

---

## ⚠️ Hinweise

- Es wird keine Datenbank verwendet – alle Aufgaben werden in einer Textdatei gespeichert.
- Das Projekt dient zu Lernzwecken (Grundlagen zu Sockets, Threads, GUI-Design und Dateiverarbeitung).

---

## 🏁 Ausblick / Erweiterungsmöglichkeiten

- Aufgaben filtern oder sortieren
- Dateibasierte Backups oder Export in andere Formate
- Server-Authentifizierung
- Webbasierter Client (z. B. mit Flask)

---

## 📜 Lizenz

Dieses Projekt ist frei verwendbar für schulische und private Zwecke.

---

**Viel Spaß beim Aufgabenplanen! 🗂️**

