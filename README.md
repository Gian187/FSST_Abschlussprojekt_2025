# Task Planner with Client/Server TCP Communication

## Description
This project is a **task management application** that allows users to create, manage, and track tasks through a graphical user interface (GUI).  
The application features **client/server communication using TCP sockets**, enabling multiple clients to interact with a central task database.

---

## Features

### 🗂️ Task Management
- Create tasks with:
  - Title
  - Category
  - Priority
  - Start date
  - Deadline
  - Status
- View all tasks in a structured list
- Delete tasks as needed

### ✅ Date Validation
- Ensures deadlines cannot be set before start dates

### 🌐 Multi-Language Support
- English 🇬🇧 and German 🇩🇪 support (selectable in CLI version)

### 🖧 Client-Server Architecture
- TCP socket communication between client and server
- Centralized task storage on server

### 🖼️ User-Friendly GUI
- Intuitive form for task creation
- Clear task display with delete functionality

---

## Technologies Used
- **Python 3**
- **Tkinter** (GUI)
- **Socket programming** (TCP)
- **File I/O** for task persistence
- **Datetime** handling

---

## File Structure

| File              | Description                                              |
|-------------------|----------------------------------------------------------|
| `main.py`         | Main application file with GUI and core functionality   |
| `addtask.py`      | Functions for task validation and file operations       |
| `Add_Function.py` | Additional task management functions (CLI version)      |
| `GUI.py`          | Alternative GUI implementation                          |
| `server.py`       | TCP server handling centralized task storage            |

---

## Getting Started

### ✅ Prerequisites
- Python 3.x
- Tkinter (usually included with Python)
- Additional package: `tkcalendar`  
  Install with:

```bash
pip install tkcalendar
