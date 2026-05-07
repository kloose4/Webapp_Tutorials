<h1>Meine erste Webapp</h1>

<h2>Schritt-für-Schritt-Anleitung</h3>
<h3>Allgemeines zu Flask:</h2>

<ul>
<li>Flask ist ein sogenanntes Micro Webframework in Python.</li>
<li>Damit lassen sich Web-Apps bauen, die Python-Code implementieren.</li>
<li>Jemand ruft also beispielsweise eine URL auf und der Python-Code entscheidet, was zurückkommt (z.B. HTML, Text, etc.)</li>
</ul>

<h3>Flask installieren:</h3>
<ul>
<li>Öffne auf der Festplatte C:\ eine Eingabeaufforderung (Du kannst nach "cmd.exe" suchen).</li>
<li>Befehl "cd C:\Program Files\Python314\Scripts" <-- Es kann sein, dass Python bei dir woanders gespeichert ist.</li>
<li>Befehl "pip install Flask"</li>
</ul>

<h3>Ein Projekt erstellen:</h3>
<ul>
<li>Erstelle einen neuen Projektordner, bspw. "Webapp".</li>
<li>Öffne diesen Ordner mit Visual Studio Code.</li>
<li>Erstelle eine erste Python-Datei, bspw. "app.py".</li>
<li><img width="826" height="154" alt="testen" src="https://github.com/user-attachments/assets/24088fc2-175b-4d62-b63b-d5129f1073fb" /></li>
</ul>

<h3>Die App ausführen und testen:</h3>
<ul>
<li>Starte die Datei "app.py".</li>
<li>Im Terminal wird die Ausgabe "Running on ..." erzeugt, und es wird eine IP-Adresse mit einem Port angezeigt (z.B. 127.0.0.1:5000)</li>
<li>Klicke diese Adresse mit "STRG" + "linke Maustaste" an.</li>
<li>Nun sollte sich dein Browser mit der Webapp öffnen.</li>
<li><img width="206" height="71" alt="testbild_browser" src="https://github.com/user-attachments/assets/4cefb264-2027-4c54-af16-e77e53d3553d" /></li>
</ul>

<h3>Die Web-App mit HTML strukturieren:</h3> 
<ul>
<li>Im Seelauf-App-Ordner erstellen wir einen Unterordner mit dem Namen "templates". Dieser Ordner muss so benannt werden, da Flask automatisch in diesem Ordner nach HTML-Dateien sucht.</li>
<li>Im Ordner "templates" erstellen wir eine HTML-Datei. Diese können wir benennen, wie wir wollen. Der Name wird jedoch zu einem späteren Zeitpunkt wieder relevant.</li>
<li>In diesem Beispiel nennen wir die Datei startseite.html</li>
<li><img width="1127" height="395" alt="html_bsp" src="https://github.com/user-attachments/assets/38b1a46d-0150-409e-b987-a6bad9ec1ce0" /></li>
</ul>

<h3>Die HTML-Datei als Template für die Web-App nutzen:</h3>
<ul>
<li>Damit die Seite mit Hilfe der HTML-Datei strukturiert wird, müssen wir die Datei app.py anpassen.</li>
<li>Dafür verwenden wir das Modul "render_template".</li>
<li>Dieses Modul importieren wir. --> "from flask import render_template"</li>
<li><img width="528" height="22" alt="screenshot render_import" src="https://github.com/user-attachments/assets/3c3e73ee-5542-4692-b233-c8e404209951" /></li>
<br>
<li>Wir ersetzen den Test-Text "Dies ist ein Test" mit render_template('startseite.html') <-- hier ist nun der Name der HTML-Datei wichtig</li>
<li>Flask wird nun statt des Test-Textes die HTML-Datei laden und anzeigen.</li>
<li>Nun können wir die Seite neu laden und schauen, ob es funktioniert hat.</li>
<li><img width="604" height="175" alt="screenshot template" src="https://github.com/user-attachments/assets/3438e046-7849-4edd-886c-99b6ce0009b2" /></li>
</ul>

<h3>Die HTML-Datei mit CSS stylen:</h3>
<ul>
<li>Das CSS-Styling funktioniert nach bekanntem Muster.</li>
<li>Es gibt in der Ordnerstruktur jedoch bei der Nutzung von Flask kleinere Unterschiede, die es zu beachten gilt.</li>
<li>Flask gibt vor, dass u.a. css-Dateien in einem sogenannten "static"-Ordner liegen muss.</li>
<li>Da im späteren Verlauf des Projekts beispielsweise auch Bilder verwendet werden, die ebenfalls im static-Ordner liegen, ist es ratsam, einen weiteren Unterordner namens "css" in static anzulegen.</li>
<br>
<li>Wir legen einen static-Unterordner in unserem Webapp-Ordner an. Darin erstellen wir einen weiteren Ordner "css".</li>
<li>Für verwendete Bilder erstellen wir den Ordner "images"</li>
<li><img width="315" height="264" alt="screenshot ordnerstruktur" src="https://github.com/user-attachments/assets/43754ee5-abad-488b-b85b-8a4722ea4c29" /></li>
<br>
<li>Im css-Unterordner erstellen wir eine Datei "styles.css".</li>
<li>Viel zu stylen gibt es in der HTML bisher nicht. Wir konzentrieren uns daher auf den Hintergrund, die Überschrift und einen Absatz.</li>
<li><img width="468" height="271" alt="screenshot css" src="https://github.com/user-attachments/assets/74fb3650-70be-4224-92ff-ea660245c39f" /></li>
<br>
<li>Nun müssen wir in der HTML-Datei kenntlich machen, dass das Styling durch die styles.css angewendet werden soll.</li>
<li>In einer Flask-Anwendung funktioniert das etwas anders, als beim herkömmlichen HTML/CSS-Styling.</li>
<li><img width="832" height="21" alt="screenshot link_rel css" src="https://github.com/user-attachments/assets/79ec1fe4-b117-4977-8a3a-f9cb3fc094f6" /></li>
<li>Die geschweiften Klammern in einer HTML-Datei werden wahrscheinlich neu für dich sein.</li>
<li>Das ist die Syntax von Jinja2, einer sogenannten Template-Engine für Python.</li>
<li>Mit Jinja2 kann man Logik (Python) und Darstellung (HTML) miteinander verknüpfen.</li>
</ul>

<h2>Du möchtest dieses Projekt übernehmen und daran weiterarbeiten?</h2>
<h3>Ein Repository klonen:</h3>
<ul>
<li>Erstelle einen neuen, leeren Ordner und öffne diesen mit Visual Studio Code.</li>
<li>Öffne in Visual Studio Code ein neues Terminal.</li>
<li>"git clone https://github.com/kloose4/Webapp_Tutorials.git"</li>
</ul>
