import sqlite3

def verbindung_herstellen():
    return sqlite3.connect("einkaufen.db")

# CRUD Operationen:

# CREATE
def produkte_hinzufügen(produkt, menge, einheit):
    verbindung = verbindung_herstellen()
    cursor = verbindung.cursor()
    cursor.execute("""
    INSERT INTO einkaufsliste (produkt, menge, einheit, erledigt)
    VALUES (?, ?, ?, ?)
    """, (produkt, menge, einheit, False))
    verbindung.commit()
    verbindung.close()

# READ
def einkaufsliste_abfragen():
    verbindung = verbindung_herstellen()
    cursor = verbindung.cursor()
    cursor.execute("SELECT * FROM einkaufsliste")
    einkaufsliste = cursor.fetchall()
    verbindung.close()
    return einkaufsliste

# UPDATE
def update_erledigt(produkt_id):
    verbindung = verbindung_herstellen()
    cursor = verbindung.cursor()
    cursor.execute("""
    UPDATE einkaufsliste
    SET erledigt = ?
    WHERE produkt_id = ?
    """, (True, produkt_id))
    verbindung.commit()
    verbindung.close()


# Tabelle erstellen
verbindung = verbindung_herstellen()
cursor = verbindung.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS einkaufsliste (
    produkt_id INTEGER PRIMARY KEY AUTOINCREMENT,
    produkt TEXT,
    menge INTEGER, 
    einheit TEXT,
    erledigt BOOLEAN           
               )
               """)

verbindung.commit() # speichert Änderungen
verbindung.close() # schließt die Verbindung
