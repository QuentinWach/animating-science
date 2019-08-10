<div align="center">
<img src="docs/Abb/Abb_5.png"></img>
</div>

# Skyhook
    
Traditionelle Raumfahrt ist teuer und äußerst Ressourcen-intensiv. Ein einfacherer Weg  ins All zu kommen ist ein sogenannter Skyhook, ein ständig rotierendes Seil, das Raumschiffe wie ein Katapult aus dem Orbit ins All schießt. Wir simulieren eine solche Infrastruktur im Sonnensystem (zunächst zwischen Erde und Mars), wobei grundlegende Fragen der Astrodynamik beantwortet werden.

---

### Referenzen
+ https://www.youtube.com/watch?v=aoMOSa9kXPw 
+ https://sites.google.com/view/quellenskyhook/
+ https://en.wikipedia.org/wiki/Skyhook_%28structure%29

### Setup
Geschrieben in `Python3.5`. Die nötigen Module finden sich in `requirements.txt` und lassen sich über `pip install` in einer virtuellen Umgebung installieren. (Achtung: Derzeit viele überflüssige Module.)

1. Installiere `Python3.5`
2. Installiere `pip`
2. Installiere `virutalenv`
3. Erstelle eine virtuelle Umgebung mit Python3.5 und wähle dieses aus
4. Lade den Projektordner herunter und wählen die dir im Terminal aus
5. Installiere die nötigen Module mit `pip install -r requirements.txt` 
6. Führe das Program mit `python run.py` aus

---

#### TODO  *Deadline: 10. Oktober 2019*
1)  [X] vereinfachte Planetebahnen (Sonne, Erde, Mars)
    1)  [X] Funktion: Planetenbahn
    2)  [X] Planetenklasse
    3)  [X] Planetenbahnen aus Klasse
    4)  [X] Animation der Planetenbewegungen
    5)  [X] Funktion: An/Aus wahre/konstante Skalierung der Radien
    6)  [ ] Plotte Skalen [km] und Zeitleiste [Tage]
    7)  [ ] Finde das nötige Format der Abbildung
2)  [ ] Einfacher Flug Raumschiff RS im Gravitationsfeld der Sonne von Erde zu Mars
    1)  [X] Gravitative Anziehung (lineare Näherung) pro Zeitrschritt durch Sonne auf Rakete
    2)  [X] Bewegungsupdate durch a. Grav + b. Eigensgeschw. pro Zeiteinheit. Stabile Elliptische Bahnen
    3)  [ ] Funktion: Suche die Abschussgeschw. und Schussdatum
    4)  [ ] Funktion (Planeten): Ermittlung der gravit. Einflusssphäre
        + https://de.wikipedia.org/wiki/Einflusssph%C3%A4re_(Astronomie)
    5)  [ ] Spline-Interpolation
    + Stärkere Verwendung analytischer Methoden vor der numerischen Näherung der Lösung dieser
3)  [ ] Tennis mit Raumschiff zwischen Mars und Erde (Nur Betrachtung der Flugbahnen)
4)  [ ] Orbit Raumschiff im Grav der Erde2
    1)  [ ] Planeten Gravitation verleihen (Feste Bahnen sollen mit den Gravbahnen übereinstimmen!)
5)  [ ] Raumschiff --> rotierender Skyhook
6)  [ ] Raumschiff Orbit um Erde mit Skyhook
7)  [ ] Raumschiff von einem Planeten zum nächsten schießen
    + Zielgeschwindigkeit des RS = Geschwindigkeit des Planeten
8)  [ ] Raumschiff mit Skyhook senden und auffangen zwischen Erde und Mars
9)  [ ] Periodischer aumtomatischer Austausch von Raumschiffen zwischen Skyhooks auf versch. Planeten

*Optional*:
+   [ ] Tatsächliche Positionen und Bahnen der Planeten + exaktes Datum
+   [ ] Betrachtung relativistischer Effekte
+   [ ] Visualisierung des Gravitationsfeldes
