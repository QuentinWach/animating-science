# Planetenblüte, 7.Januar 2019
"""
Die Quadrate der Umlaufzeiten stehen im gleichen Verhältnis 
wie die Kuben der großen Halbachsen.
"""

import matplotlib.pyplot as plt
import numpy as np

# Umlauzeiten der Planeten
U_Merkur = 87.969
U_Venus = 224.701
U_Erde =  365.256
U_Mars =  686.980

# Abstände der Planeten zur Sonne
R_Merkur = 58000000
R_Venus = 108000000
R_Erde =  150000000
R_Mars =  228000000

# Positionen
x_Erde = []; y_Erde = []
x_Mars = []; y_Mars = []

# Zeitspanne
TIME = 1000 * 12
# Zeitschritte
STEP = 1

# Generiere Umlaufdaten
for T in range(TIME):
    # Erde
    x_Erde.append(R_Erde * np.sin(STEP * T * 2 * np.pi / U_Erde))
    y_Erde.append(R_Erde * np.cos(STEP * T * 2 * np.pi / U_Erde))
    # Mars
    x_Mars.append(R_Mars * np.sin(STEP * T * 2 * np.pi / U_Mars))
    y_Mars.append(R_Mars * np.cos(STEP * T * 2 * np.pi / U_Mars))

# Erstelle die Figur
fig = plt.figure(dpi=300)
ax = plt.axes([0,0,1,1])
ax.set_facecolor("white")
ax.set_aspect("equal")

# Verbindungslinien
for p in range(len(x_Erde)):
    if p % 10 == 0:
        plt.plot([y_Erde[p],y_Mars[p]],[x_Erde[p],x_Mars[p]], ":", linewidth=0.175, color="black")

plt.plot(y_Erde[:int(U_Erde)], x_Erde[:int(U_Erde)], "-.", linewidth=0.3, color="black")
plt.plot(y_Mars[:int(U_Mars)], x_Mars[:int(U_Mars)], "--", linewidth=0.3, color="black")
plt.plot(0,0, "o", color="black", markersize=2)

plt.axis("off")
fig.savefig("Abbildung.png", bbox_inches=0)