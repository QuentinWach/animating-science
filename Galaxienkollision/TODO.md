# TODO

Die großen Probleme hier sind klar:
1. Berechnung zu ineffizient (da Brute Force)
2. Wenn Körper sich zu nahe kommen, werden sie zu stark beschleunigt!

#### Numerical Computational Methods
+ [X] Gravity-Smoothing: Modifikation der Newt.Grav.-Formel
+ [X] Only calculate particle interactions between random particles. Randomly drop particle interactions for each step. --> weird latency/shadow effect --> stabelizes oszillating centered nebulas
+ [X] Only randomly drop particle interactions randomly between particles that move very slowly --> only increases computational cost while creting a bad resolution
+ [X] Only randomly drop particle interactions between particles where gravitational pull is week i.e. they are far away from each other

#### Emperical Computational Methods
Predicting the future from experience.
+ [ ] Create a neural network to learn to predict any gravity sim with given parameters and positions

# LOG

#### 22.Jan
So wie in der Festkörperphysik das Zusammenspiel der Teilchen zu Phäno-
menen führen, wie Schwingungen, Brechung des Lichts oder Leitung elektrischen Stroms, so scheint mir zeigt sich auch ähnliche Emergenz
in der Wechselwirkung von Teilchen, welche äußerst weit von einander entfernt sind. Homogen verteilte Massen im Raum ziehen sich durch ihre Gravitation so an, dass sich zunächst Nebel, das Fäden aus Sternen, dann Cluster, dann kreisende Galaxien bilden. Und im Fall der Körper zum gemeinsamen Schwerpunkt lassen sich Muster entdecken, derartig einfach, dass ich mich frage, warum diese übergeordneten Strukturen nicht beschrieben werden, anstatt die zugrundeliegende Kraft. 
In Galaxien häufen sich einzelne Sterne in kontinuirlich erscheinenden Wellen an, welche Arme bilden. Warum die Bahnkurven von millionen von Sternen berechnen, wenn doch sicher eine einfache Beschreibung dieser übergeordneten Strukturen möglich ist.
**Lässt sich ein Sternenhaufen als ein einzelner Körper modellieren?**
In 2D wirkt es oftmals, als betrachte man das wilde Falten eines Tuchs, nicht die Bewegungen von Sternen.

# TODO

# 760 x 764 Pixel
+ [ ] plot stats on frame
+ [ ] simplify code make it production ready + documentation 
    1. Initialize System
    2. Define Simulation Type
    3. Define Rendering Options
+ [ ] add timemeasurement and loading bars
+ [ ] enable saving and loading of simulations to test, stop, 
      and continue experimentation!
+ [ ] 3D
+ [ ] OpenGL
+ [ ] nicht linear, sondern Eulerverfahren zur Interpolation mit vergangenen Schritten!
+ [ ] Barnes-Hut (BH)
+ [ ] Fast multipole method (FMM)
+ [ ] BH + FMM
+ [ ] Paticle-Mesh-Method: https://observablehq.com/@rreusser/2d-n-body-gravity-with-poissons-equation,
+ [ ] P^3 M-Method: https://en.m.wikipedia.org/wiki/P3M
+ [ ] Moving Mesh, Volker Springer
---
+ [ ] consider particle interactions
---
+ [ ] GITHUB PROJECT PAGE

# possible colormaps
copper
gist_heat
afmhot
pink
bone gray

plasma
inferno
magma

cividis