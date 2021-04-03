import sqlite3
from todos import TaskManager, Action_add

conn = sqlite3.connect('ma_base.db')

cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS taches(
     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     name TEXT,
     description TEXT,
     numero INTEGER,
     statut TEXT
)
""")

conn.commit()

cursor.execute("""
INSERT INTO taches(name, description, numero, statut) VALUES(?, ?, ?, ?)""", ("add", "first task", 1, "à faire"))

conn.commit()

cursor.execute("""SELECT name, description, numero, statut FROM taches""")
user1 = cursor.fetchone()
print(user1)

conn.commit()

conn.close()