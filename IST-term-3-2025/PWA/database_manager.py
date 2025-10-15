import sqlite3 as sql

DB_PATH = r"C:\Users\Annec\.vscode\IST-term-3-2025\PWA\database\data_source.db"

def listReminders():
    con = sql.connect(DB_PATH)
    cur = con.cursor()
    data = cur.execute("SELECT * FROM reminders").fetchall()
    con.close()
    return data

def addReminder(title, description, due_date):
    con = sql.connect(DB_PATH)
    cur = con.cursor()
    cur.execute(
        "INSERT INTO reminders (title, description, due_date) VALUES (?, ?, ?)",
        (title, description, due_date),
    )
    con.commit()
    con.close()

def completeReminder(reminder_id):
    con = sql.connect(DB_PATH)
    cur = con.cursor()
    cur.execute("UPDATE reminders SET completed = 1 WHERE id = ?", (reminder_id,))
    con.commit()
    con.close()

def deleteReminder(reminder_id):
    try:
        con = sql.connect(DB_PATH)
        cur = con.cursor()
        cur.execute("DELETE FROM reminders WHERE id = ?", (reminder_id,))
        con.commit()
        con.close()
        print(f"🗑️ Deleted reminder with ID {reminder_id}")
    except Exception as e:
        print("❌ Error deleting reminder:", e)

def createListsTable():
    con = sql.connect(DB_PATH)
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS lists (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT
        )
    """)
    con.commit()
    con.close()

def addList(name, description=None):
    con = sql.connect(DB_PATH)
    cur = con.cursor()
    cur.execute("INSERT INTO lists (name, description) VALUES (?, ?)", (name, description))
    con.commit()
    con.close()

def listLists():
    con = sql.connect(DB_PATH)
    cur = con.cursor()
    data = cur.execute("SELECT * FROM lists").fetchall()
    con.close()
    return data

createListsTable()

def deleteList(list_id):
    try:
        con = sql.connect(DB_PATH)
        cur = con.cursor()
        cur.execute("DELETE FROM lists WHERE id = ?", (list_id,))
        con.commit()
        con.close()
        print(f"🗑️ Deleted list with ID {list_id}")
    except Exception as e:
        print("❌ Error deleting list:", e)
