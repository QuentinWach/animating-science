# TODO

Die großen Probleme hier sind klar:
1. Berechnung zu ineffizient (da Brute Force)
2. Wenn Körper sich zu nahe kommen, werden sie zu stark beschleunigt!

#### Numerical Computational Methods
+ [X] Gravity-Smoothing: Modifikation der Newt.Grav.-Formel
+ [X] Only calculate particle interactions between random particles. Randomly drop particle interactions for each step. --> weird latency/shadow effect --> stabelizes oszillating centered nebulas
+ [X] Only randomly drop particle interactions randomly between particles that move very slowly --> only increases computational cost while creting a bad resolution
+ [X] Only randomly drop particle interactions between particles where gravitational pull is week i.e. they are far away from each other
+ [ ] Limitierung der Schrittgröße
+ [ ] Barnes-Hut

---
#### Emperical Computational Methods
Predicting the future from experience.
+ [ ] Create a neural network to learn to predict any gravity sim with given parameters and positions
