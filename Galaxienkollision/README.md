# Gravitation

Ziel dieses kleinen Projektes ist letztendlich eine sehr rudimentäre Simulation der Kollision zweier Galaxien.
Hier aber zunächst einfach ein paar erste Tests:
<div align="center">
<img src="./animation.gif" align="left"></img>
<img src="./animation2.gif" align="right"></img>
<img src="./animation3.gif"></img>
</div>
Die großen Probleme hier sind klar:
1) Berechnung zu ineffizient (da Brute Force)
2) Wenn Körper sich zu nahe kommen, werden sie zu stark beschleunigt!

### TODO:
+ [ ] Limitierung der Schrittgröße
+ [ ] Gravity-Smoothing: Modifikation der Newt.Grav.-Formel
+ [ ] Barnes-Hut
