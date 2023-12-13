#uvicorn main:app --reload

from fastapi import FastAPI
import sqlite3
    
#createTable("toto", ["col1 INT", "col2 TEXT"])
def createTable(table, colonnes):
    cur = conn.cursor()
    cur.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table}'")
    existing_table = cur.fetchone()
    if not existing_table:
        colonnes_str = ", ".join(colonnes)
        cur.execute(f"CREATE TABLE {table} ({colonnes_str})")
    conn.commit()
    cur.close()


#select("toto", ["col1", "col2"])
def select(table, colonnes, clause=None):
    colonnes_str = ", ".join(colonnes)
    query = f"SELECT {colonnes_str} FROM {table}"
    
    if clause:
        query += f" WHERE {clause}"

    cur = conn.cursor()
    cur.execute(query)
    return cur.fetchall()

#insertIntoTable("toto", {"col1": 42, "col2": "Hello"})
def insertIntoTable(table, values):
    cur = conn.cursor()
    colonnes_str = ", ".join(values.keys())
    values_str = ", ".join([f"'{value}'" for value in values.values()])
    cur.execute(f"INSERT INTO {table} ({colonnes_str}) VALUES ({values_str})")
    conn.commit()
    cur.close() 

#update_table("citations", {"citation": "Nouvelle citation"}, {"id": 1})
def update_table(table, values, condition):
    # Créer une connexion à la base de données (remplacez 'example.db' par le nom de votre base de données)
    cur = conn.cursor()

    # Construire la requête UPDATE
    set_clause = ", ".join([f"{key} = '{value}'" for key, value in values.items()])
    condition_clause = " AND ".join([f"{key} = '{value}'" for key, value in condition.items()])
    cur.execute(f"UPDATE {table} SET {set_clause} WHERE {condition_clause}")

    # Valider la transaction et fermer la connexion
    conn.commit()
    cur.close()   

conn = sqlite3.connect('dataBase.db')

app = FastAPI()

createTable("citations", ["id INT", "citation TEXT"])
#insertIntoTable("citations", {"id": 2, "citation": "Couper la poire en deux"})
update_table("citations", {"citation": "Couper la poire&en deux"}, {"id": 2})

@app.get("/citations")
async def get_citations():
    citations = select("citations", "*")
    citations_cleaned = [{'id': row[0], 'citation': row[1].replace('&', ' ')} for row in citations]
    return {'citations':citations_cleaned}, 200

@app.get("/citation/{id}")
async def get_citation(id: int):
    citations = select("citations", "*", f"id = {id}")
    citations_cleaned = [{'id': row[0], 'citation': row[1].replace('&', ' ')} for row in citations]
    return {'citations':citations_cleaned}, 200
