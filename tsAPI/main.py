#uvicorn main:app --reload
from random import seed, randint
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
    
class CitationCreate(BaseModel):
    citation: str

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

def getSizeTable(table):
    cur = conn.cursor()
    return int(cur.execute(f"SELECT COUNT(*) FROM '{table}'").fetchone()[0])
    #return len(select(table, "*"))

def delete_from_table(table, condition):
    try:
        condition_clause = " AND ".join([f"{key} = '{value}'" for key, value in condition.items()])
        query = f"DELETE FROM {table} WHERE {condition_clause}"

        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        cur.close()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

conn = sqlite3.connect('dataBase.db')

app = FastAPI()

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

@app.get("/ranCitation")
async def get_random_citation():
    citations = select("citations", "*")

    ran1 = randint(0,getSizeTable("citations")-1)
    ran2 = randint(0,getSizeTable("citations")-1)
    
    while ran2 == ran1:
        ran2 = randint(0,getSizeTable("citations")-1)

    citaDebut = citations[ran1][1]
    citaFin = citations[ran2][1]
    
    result = citaDebut.split('&')[0] + " " +  citaFin.split('&')[1]

    return {'citations':result}, 200

@app.post("/addCitation")
async def add_citation(citation_data: CitationCreate):
    try: 
        nouvelle_citation = citation_data.citation
        insertIntoTable("citations", {"citation": nouvelle_citation})
        return {"message": "Citation ajoutée avec succès"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.delete("/deleteCitation")
async def del_citation(citation_id: int):
    try:
        existing_citation = select("citations", ["id"], f"id = {citation_id}")
        if not existing_citation:
            raise HTTPException(status_code=404, detail=f"Citation avec l'ID {citation_id} non trouvée")

        delete_from_table("citations", {"id": citation_id})

        return {"message": f"Citation avec l'ID {citation_id} supprimée avec succès"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))