import sqlite3

conn = sqlite3.connect("habits.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS habits (
    username TEXT,
    day TEXT,
    gym BOOLEAN,
    study BOOLEAN,
    wake BOOLEAN,
    PRIMARY KEY (username, day)
)
""")

conn.commit()
conn.close()
