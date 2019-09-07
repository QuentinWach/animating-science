# Elektrodynamik mehrerer Teilchen auf einer Ebene
# Quentin Wach, 5.September 2019

import numpy as np
import matplotlib.pyplot as plt
import inspect


# Raster
X,Y = np.meshgrid( np.arange(-4,4,.01), np.arange(-4,4,.01) )

# Vektorfeld einer Ladung
def q_field(q,x,y):
    """
    q: Ladung, 1 oder -1
    x,y: Position auf der x,y-Achse
    """
    # Definition des Feldes im Raster
    Ex = q/(4*np.pi)* (X+x)/((X+x)**2 + (Y+y)**2)**1.5
    Ey = q/(4*np.pi)* (Y+y)/((X+x)**2 + (Y+y)**2)**1.5
    
    return Ex, Ey, q, x, y

# Gesamtes Feld
def total_field(L):
    total_x = 0
    total_y = 0
    for field in L:
        e = 0
        while e <= 2:
            total_x += field[0]
            total_y += field[1]
            e += 1
    return total_x, total_y

# Zeige die Ladungen und das Feld
def vis(L):
    plt.style.use("default")
    plt.style.use("seaborn-dark")
    plt.style.use("grayscale")
    
    # Definiere das Gesamte Feld mit gegebener Ladungskonfiguration
    x_total = total_field(L)[0]
    y_total = total_field(L)[1]
    
    # Zeige das Feld
    fig = plt.figure(figsize=(7,7), dpi=100)
    fig.patch.set_facecolor('white')
    plt.xticks([])
    plt.yticks([])
    
    # Zeige die Ladungen
    white = (1,1,1,1)
    blue = (0.3, 0.5, 0.8,1)
    red = (1,0.5,0.5,1)
    for field in L:
        if field[2] < 0:
            plt.plot(-field[3], -field[4], "o", color=white, zorder=40, markersize=25)
            plt.plot(-field[3], -field[4], "o", color=blue, zorder=60, markersize=10)
        else:
            plt.plot(-field[3], -field[4], "o", color=white, zorder=40, markersize=25)
            plt.plot(-field[3], -field[4], "o", color=red, zorder=60, markersize=10)
    
    # Plotte alles zu zeigende
    plt.streamplot(X,Y,x_total,y_total, color = (0,0,0,1), cmap="inferno",
              density=1.5, linewidth=1)
    plt.show()

#-----------------------------------------

# anfängliche Ladungskonfiguration
L = [q_field(-1,1.4,0.2),
     q_field(1,-3,0.7),
     q_field(-1,-1.4,-2.1),
     q_field(1,3.6,-3)]

L = [q_field(-1,1,0),
     q_field(1,-1,0)]

vis(L)


#-----------------------------------------
"""
Um die Ladungspositionen zu animieren, müssen hier für jeden Zeitschritt L angepasst werden.
"""
"""
# Animiere die Ladungen durch Coulomb-Kraft
def Coulomb(T_1, T_2):
    s1 = 0
    s2 = 0
    
    c = 

    return s1, s2
"""
