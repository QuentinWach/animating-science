# Random Walker ThP4 14.Mai 2020
# Quentin Wach
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.ticker as ticker
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)
import numpy as np
import math
np.random.seed(14520)

# figure setup
matplotlib.style.use('ggplot')
fig, ax = plt.subplots(1, figsize=(6,2.7), dpi=300)

# HYPERPARAMETER
P = 0.3     # Schritt nach Links
Q = 1 - P   # Schritt nach Rechts
T = (10,100,1000)     # Zeitschritte
E = 3000              # Experimente

# DATEN
a = 0
for t in T:
    # Verteilung
    X = []
    for e in range(E):
        x = 0       # Startpunkt
        for i in range(t):
            if np.random.random_sample() <= P:
                x -= 1
            else:
                x += 1
        X.append(x)
    # Breite der Verteilung
    # B = abs(min(X)) +  abs(max(X))
    a += 1
    ax.hist(X, 9*a, density=True, align="mid", color="black", zorder=30)

# Axes & Grid
ax.set_ylim(0,0.2)
ax.xaxis.set_major_locator(ticker.MultipleLocator(50))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(10))
ax.grid(b=True, color='white', linestyle="--", linewidth=0.5, zorder=0)

# Label & Text
plt.ylabel("Wahrscheinlichkeit", size=9)
plt.xlabel(r"Schritte $x$", size=9)
plt.text(-1, 0.162, r"$P_1[x(t=10)]$")
plt.text(35, 0.075, r"$P_2[x(t=100)]$")
plt.text(395, 0.03, r"$P_3[x(t=1000)]$")

# Render
plt.tight_layout()
plt.savefig("Abb_1.png", bbox_inches="tight")