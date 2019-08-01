# Module
import numpy as np
import matplotlib.pyplot as plt
import massen

# Massen der Körper
M_SUN = 0
M_EARTH = 0
M_MARS = 0 

#-----------------------------------------------------------------------------
class Planet():
    def init(self, m, ut, r):
        """
        Masse: m
        Umlaufzeit: ut
        Entfernung zur Sonne: r
        """
        self.m = m
        self.ut = ut
        self.r = r

    # Planetenbahn
    def planet_orbit(r, ut, t):
        """
        t:  spez. Zeitpunkt
        """
        pt = 2 * np.pi * t / T
        x = R * np.sin(pt)
        y = R* np.cos(pt)
        return x, y

    # Sammlung der Datenpunkte
    x_past = []
    y_past = []










#-----------------------------------------------------------------------------
# Animiere die Simulation

def animate(i):
    # Koordinaten der drei Punkte
    thisx = [0, x1[i], x2[i]]
    thisy = [0, y1[i], y2[i]]

    # Drucke die Koordinaten im Terminal
    print("x(" + str(i) + ") = " + str(thisx))
    print("y(" + str(i) + ") = " + str(thisy))

    # Merke vergangene Koordinaten
    if i <= 1000:
      pastx.append(thisx[2]); pasty.append(thisy[2])
    else:
      pastx.pop(0); pasty.pop(0)
      pastx.append(thisx[2]); pasty.append(thisy[2])

    # Datenupdate
    line.set_data(thisx, thisy)
    dots.set_data(pastx, pasty)

    # Zeittextupdate
    time_text.set_text(time_template % (i*dt))

    return line, dots, time_text















#-----------------------------------------------------------------------------
# Starte die Simulation
if __name__ == '__main__':
    anim = animation.FuncAnimation(fig, animate, 
        frames=np.arange(0, len(y), 1), interval=15)
    #anim.save('pendel.gif', dpi=80, writer='imagemagick') 

    plt.show()