# Module
import numpy as np
import matplotlib.pyplot as plt

# Massen der Körper [kg]
M_SUN = 0
M_EARTH = 0
M_MARS = 0 
# Umlaufzeiten [Tage]
UT_SUN = 1
UT_EARTH = 365
UT_MARS = 720
# Abstände zur Sonne [1000km]
D_SUN = 0
D_EARTH = 496000000
D_MARS = 1.5 * D_EARTH

# Radien der Körper [1000km]
R_SUN =     69634200
R_EARTH =   6.371001
R_MARS =    3.389500

#-----------------------------------------------------------------------------
class Planet:
    def __init__(self, M, UT, D, R):
        """
        Masse: m
        Umlaufzeit: ut
        Entfernung zur Sonne: d
        Radius des Körpers: r
        """
        self.m = M
        self.ut = UT
        self.d = D
        self.r = R
        
        # Sammlung der Datenpunkte
        self.X = []
        self.Y = []

    # Planetenbahn
    def planet_orbit(self, t):
        """
        t:  spez. Zeitpunkt
        """
        self.pt = 2 * np.pi * t / self.ut
        x = self.d * np.sin(self.pt)
        y = self.d * np.cos(self.pt)
        return x, y

# Erstelle Planetenobjekte
sun = Planet(M_SUN, UT_SUN, D_SUN, R_SUN)
earth = Planet(M_EARTH, UT_EARTH, D_EARTH, R_EARTH)
mars = Planet(M_MARS, UT_MARS, D_MARS, R_MARS)

# Sammle die Positionen der Planeten im Zeitverlauf
TIME = 1000
for t in range(TIME):
    # Sonne
    #sun.X.append(sun.planet_orbit(t)[0])
    #sun.Y.append(sun.planet_orbit(t)[1])
    # Erde
    earth.X.append(earth.planet_orbit(t)[0])
    earth.Y.append(earth.planet_orbit(t)[1])    
    # Mars
    mars.X.append(mars.planet_orbit(t)[0])
    mars.Y.append(mars.planet_orbit(t)[1])  
   
#----------------------------------------------------------------------------- 
# Plotte

# Plotdesign
plt.style.use("default")
plt.style.use("seaborn-dark")
plt.style.use("grayscale")
fig = plt.figure(figsize=(7,7), dpi=120)
fig.patch.set_facecolor('white')
fig.canvas.set_window_title('Skyhook')
plt.xticks([])
plt.yticks([])

# Planetenskalierung
trueScale = False
m_scale = 10**(-7)
def marker_scale(R):
    if trueScale == 1:
        return R * m_scale
    else:
        return 10

# Sonne
plt.plot(0,0, "o", color="#ffbd5b", markersize=marker_scale(R_SUN))
# Erde
plt.plot(earth.X, earth.Y) # Bahn
plt.plot(earth.X[100], earth.Y[100], "o", color="#618abf", 
         markersize=marker_scale(R_EARTH)) # Körper
# Mars
plt.plot(mars.X, mars.Y) # Bahn
plt.plot(mars.X[100], mars.Y[100], "o", color="#f2663c",
         markersize=marker_scale(R_MARS)) # Körper
plt.show()


#-----------------------------------------------------------------------------
# Animiere die Simulation
"""
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
"""