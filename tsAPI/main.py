from fastapi import FastAPI
import sqlite3

conn = sqlite3.connect('dataBase.db')

cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS citations (
        id INTEGER PRIMARY KEY,
        citation TEXT,
    )
''')

cur.execute("INSERT INTO citations (citation) VALUES (?)", ('C\'est la goute d\'eau qui fait déborder le vase.'))


app = FastAPI()

donnees = {
    'lieux': [
        'Paris',
        'Lyon',
        'Marseille',
        'Montpellier',
        'Toulon',
        'Lilles',
        'Nantes']
}

@app.get("/citations")
async def get_citation():
    cur.execute("SELECT * FROM citations")
    citations = cur.fetchall()
    return {'citations':citations}, 200

