from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import date
import sqlite3

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class HabitEntry(BaseModel):
    username: str
    gym: bool
    study: bool
    wake: bool

@app.post("/submit")
def submit(entry: HabitEntry):
    today = date.today().isoformat()
    conn = sqlite3.connect("habits.db")
    cur = conn.cursor()
    cur.execute("""
        INSERT OR REPLACE INTO habits (username, day, gym, study, wake)
        VALUES (?, ?, ?, ?, ?)
    """, (entry.username, today, entry.gym, entry.study, entry.wake))
    conn.commit()
    conn.close()
    return {"status": "ok"}

@app.get("/progress")
def progress():
    today = date.today().isoformat()
    conn = sqlite3.connect("habits.db")
    cur = conn.cursor()
    cur.execute("""
        SELECT username, gym, study, wake FROM habits WHERE day=?
    """, (today,))
    data = cur.fetchall()
    conn.close()
    return {"progress": data}
