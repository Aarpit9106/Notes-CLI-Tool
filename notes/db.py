import sqlite3
import os
import datetime
from pathlib import Path

DB_FILE = os.path.expanduser("~/.notes_cli.db")

def get_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    c = conn.cursor()
    c.executescript("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            tags TEXT,
            category TEXT,
            mood TEXT,
            is_favorite INTEGER DEFAULT 0,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        CREATE TABLE IF NOT EXISTS links (
            source_id INTEGER,
            target_id INTEGER,
            PRIMARY KEY (source_id, target_id),
            FOREIGN KEY(source_id) REFERENCES notes(id) ON DELETE CASCADE,
            FOREIGN KEY(target_id) REFERENCES notes(id) ON DELETE CASCADE
        );
        CREATE TABLE IF NOT EXISTS future_messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            target_date DATE NOT NULL,
            is_delivered INTEGER DEFAULT 0,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );
    """)
    conn.commit()
    conn.close()

def add_note(content, tags="", category="", mood="", is_favorite=0):
    conn = get_connection()
    c = conn.cursor()
    c.execute(
        "INSERT INTO notes (content, tags, category, mood, is_favorite, created_at, updated_at) VALUES (?, ?, ?, ?, ?, datetime('now', 'localtime'), datetime('now', 'localtime'))",
        (content, tags, category, mood, is_favorite)
    )
    conn.commit()
    note_id = c.lastrowid
    conn.close()
    return note_id

def get_notes(limit=None, order_by="updated_at DESC"):
    conn = get_connection()
    c = conn.cursor()
    query = f"SELECT * FROM notes ORDER BY {order_by}"
    if limit:
        query += f" LIMIT {limit}"
    c.execute(query)
    notes = c.fetchall()
    conn.close()
    return notes

def get_note(note_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM notes WHERE id = ?", (note_id,))
    note = c.fetchone()
    conn.close()
    return note

def update_note(note_id, **kwargs):
    if not kwargs:
        return
    conn = get_connection()
    c = conn.cursor()
    kwargs['updated_at'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    fields = ", ".join([f"{k} = ?" for k in kwargs.keys()])
    values = list(kwargs.values())
    values.append(note_id)
    c.execute(f"UPDATE notes SET {fields} WHERE id = ?", values)
    conn.commit()
    affected = c.rowcount
    conn.close()
    return affected > 0

def delete_note(note_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    conn.commit()
    affected = c.rowcount
    conn.close()
    return affected > 0

def search_notes(keyword="", tag="", category="", date_str="", mood=""):
    conn = get_connection()
    c = conn.cursor()
    query = "SELECT * FROM notes WHERE 1=1"
    params = []
    
    if keyword:
        query += " AND content LIKE ?"
        params.append(f"%{keyword}%")
    if tag:
        query += " AND tags LIKE ?"
        params.append(f"%{tag}%")
    if category:
        query += " AND category = ?"
        params.append(category)
    if mood:
        query += " AND mood = ?"
        params.append(mood)
    if date_str:
        query += " AND date(created_at) = ?"
        params.append(date_str)
        
    query += " ORDER BY updated_at DESC"
    c.execute(query, params)
    notes = c.fetchall()
    conn.close()
    return notes

def link_notes(id1, id2):
    conn = get_connection()
    c = conn.cursor()
    try:
        # Link both ways for simplicity or just one way? Graph usually undirected for notes
        c.execute("INSERT OR IGNORE INTO links (source_id, target_id) VALUES (?, ?)", (id1, id2))
        c.execute("INSERT OR IGNORE INTO links (source_id, target_id) VALUES (?, ?)", (id2, id1))
        conn.commit()
        success = True
    except Exception:
        success = False
    finally:
        conn.close()
    return success

def get_linked_notes(note_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute('''
        SELECT n.* FROM notes n 
        JOIN links l ON n.id = l.target_id 
        WHERE l.source_id = ?
    ''', (note_id,))
    notes = c.fetchall()
    conn.close()
    return notes

def add_future_message(content, target_date):
    conn = get_connection()
    c = conn.cursor()
    c.execute(
        "INSERT INTO future_messages (content, target_date) VALUES (?, ?)",
        (content, target_date)
    )
    conn.commit()
    conn.close()

def get_undelivered_future_messages():
    conn = get_connection()
    c = conn.cursor()
    today = datetime.date.today().isoformat()
    c.execute(
        "SELECT * FROM future_messages WHERE is_delivered = 0 AND date(target_date) <= ?",
        (today,)
    )
    msgs = c.fetchall()
    conn.close()
    return msgs

def mark_future_message_delivered(msg_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute("UPDATE future_messages SET is_delivered = 1 WHERE id = ?", (msg_id,))
    conn.commit()
    conn.close()
