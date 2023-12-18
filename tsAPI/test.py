from main import *
import sqlite3
conn = sqlite3.connect('dataBase.db')

citations = select("citations", "*")
ran1 = 0#randint(0,getSizeTable("citations")-1)
ran2 = 1#randint(0,getSizeTable("citations")-1)

citaDebut = citations[ran1][1]
print("debut "+citaDebut)
citaFin = citations[ran2][1]
print("fin "+citaFin)
print( citaDebut.split('&')[0] + " " +  citaFin.split('&')[1])