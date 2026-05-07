from flask import Flask, render_template, request
import db

app = Flask(__name__)
@app.route ( "/" )
def startseite ( ):
    return render_template ("einkaufen.html") # Seite "einkaufen.html" wird geladen, wenn die URL aufgerufen wird.

@app.route( "/create", methods=["POST"] )
def create():
    produkt = request.form["produkt"]  # Daten vom Client (einkaufen.html) empfangen
    menge = request.form["menge"]
    einheit = request.form["einheit"]
    db.produkte_hinzufügen(produkt, menge, einheit)  # Zugriff auf db.py

    return render_template("einkaufen.html") # Seite wird neu geladen.

@app.route( "/update", methods=["POST"] )
def update():
    produkt_id = request.form["produkt_id"]
    db.update_erledigt(produkt_id)
    return render_template("einkaufen.html") # Seite wird neu geladen.


@app.route( "/read", methods=["GET"] )
def read():
    produkte =db.einkaufsliste_abfragen()
    return render_template("einkaufen.html", produkte=produkte) # Seite wird neu geladen, Daten aus DB werden übergeben.

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port=8080, debug=True)