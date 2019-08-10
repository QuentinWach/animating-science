# Module
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

# Gravitatioskonstante [m³/(kg * s²)]
G = 6.67430 * 10**(-9)
# Massen der Körper [kg]
M_SUN = 1.98 * (10**30)
M_EARTH = 0
M_MARS = 0 
M_ROC = 0
M_2 = 0
M_3 = 0
M_4 = 0
M_5 = 0
M_6 = 0
M_7 = 0
M_8 = 0
M_9 = 0
# Umlaufzeiten [Tage]
UT_SUN = 1
UT_2 = 88
UT_3 = 225
UT_EARTH = 365
UT_MARS = 730
UT_6 = 12*365
UT_7 = 29*365
UT_8 = 84*365
UT_9 = 164*365
# Abstände zur Sonne [1km]
D_SUN = 0
D_2 = 57900000
D_3 = 108000000
D_EARTH = 150000000 
D_MARS = 228000000 
D_6 = 778000000
D_7 = 1426000000
D_8 = 2870000000
D_9 = 4496000000
# Radien der Körper [1km]
R_SUN =   1392700/2
R_2 =       4840/2
R_3 =      12200/2
R_EARTH =   6371.001
R_MARS =    3389.500
R_6 = 142870/2
R_7 = 120670/2
R_8 = 51000/2
R_9 = 49200/2

R_ROC = 0.05

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
        x = self.d * np.cos(self.pt)
        y = self.d * np.sin(self.pt)
        return x, y

# Erstelle Planetenobjekte
sun = Planet(M_SUN, UT_SUN, D_SUN, R_SUN)
merkur = Planet(M_2, UT_2, D_2, R_2)
venus = Planet(M_3, UT_3, D_3, R_3)
earth = Planet(M_EARTH, UT_EARTH, D_EARTH, R_EARTH)
mars = Planet(M_MARS, UT_MARS, D_MARS, R_MARS)
jupiter = Planet(M_6, UT_6, D_6, R_6)
saturn = Planet(M_7, UT_7, D_7, R_7)
uranus = Planet(M_8, UT_8, D_8, R_8)
neptun = Planet(M_9, UT_9, D_9, R_9)
# Planetenliste (ohne Sonne)
planets = [earth,mars]

class Rakete:
    def __init__(self):
        # Sammlung der Positionen
        self.X = []
        self.Y = []
        # Sammlung der Geschwindigkeiten
        self.Vx = []
        self.Vy = []
        # Initialisiere die Startbedingungen (t=0)
        self.vx_start = 0
        # 1.093 : Hofmann zum Mars
        # 0.8
        self.vy_start = 1 *  (D_EARTH * 2 * np.pi) / UT_EARTH
        self.x_start = D_EARTH
        self.y_start = 0
        self.X.append(self.x_start)
        self.Y.append(self.y_start)
        self.Vx.append(self.vx_start)
        self.Vy.append(self.vy_start)

    def shoot(self, t):
        sonnenwinkel_x = self.X[t-1]/((self.X[t-1]**2 + self.Y[t-1]**2))**0.5
        sonnenwinkel_y = self.Y[t-1]/((self.X[t-1]**2 + self.Y[t-1]**2))**0.5
        s1_x = -(G * M_SUN)/(2*(self.X[t-1]**2 + self.Y[t-1]**2)) * sonnenwinkel_x
        s1_y = -(G * M_SUN)/(2*(self.X[t-1]**2 + self.Y[t-1]**2)) * sonnenwinkel_y
        # Berechne Schritt aus Eigengeschwindigkeitsvektor
        s2_x = self.Vx[t-1]
        s2_y = self.Vy[t-1]
        # Berechne Gesamtschritt
        s_x = s1_x + s2_x
        s_y = s1_y + s2_y
        # Füge neue Position der Sammlung der Datenpunkte hinzu
        self.X.append(self.X[t-1] + s_x)
        self.Y.append(self.Y[t-1] + s_y)
        # Füge die neuen Geschwindigkeiten den Datenpunkten hinzu
        self.Vx.append(self.X[t] - self.X[t-1])
        self.Vy.append(self.Y[t] - self.Y[t-1])

# Erstelle Raketenobjekt        
rocket = Rakete()

# Sammle die Positionen der Objekte im Zeitverlauf
TIME = 730#730 #UT_EARTH * UT_MARS #for perfect looping
for t in range(TIME):
    # Sonne
    #sun.X.append(sun.planet_orbit(t)[0])
    #sun.Y.append(sun.planet_orbit(t)[1])
    # Erde
    #earth.X.append(earth.planet_orbit(t)[0])
    #earth.Y.append(earth.planet_orbit(t)[1])    
    # Mars
    #mars.X.append(mars.planet_orbit(t)[0])
    #mars.Y.append(mars.planet_orbit(t)[1])
    for planet in planets:
        planet.X.append(planet.planet_orbit(t)[0])
        planet.Y.append(planet.planet_orbit(t)[1])

for t in range(668):
    # Rakete
    rocket.shoot(t+1)

#----------------------------------------------------------------------------- 
# Plotdesign
plt.style.use("default")
plt.style.use("seaborn-dark")
plt.style.use("grayscale")
fig, ax = plt.subplots(figsize=(8,8),dpi=120) #figsize=(7,7)
fig.patch.set_facecolor('white')
fig.canvas.set_window_title('Skyhook')
plt.xticks([])
plt.yticks([])

# Zeige die momentane Zeit
#time_template = 'Tag %1.f'
#time_text = ax.text(1, 1, '', transform=ax.transAxes, bbox=dict(facecolor='white', alpha=0.5))

# Planetenskalierung
trueScale = False
m_scale = 10**(-7)
def marker_scale(R):
    if trueScale == 1:
        return R * m_scale
    else:
        return 10

# Sonne
plt.plot(0,0, "o", color="#ffbd5b") #marker_scale(R_SUN)
# Planetenbahnen
for planet in planets:
    plt.plot(planet.X, planet.Y, color="#bababa") # Bahn
# Planetenbewegungen
#merkur_plot, = ax.plot(merkur.X[0], merkur.Y[0], "o", color="#e2a973")
#venus_plot, = ax.plot(venus.X[0], venus.Y[0], "o", color="#e5bc5b")
earth_plot, = ax.plot(earth.X[0], earth.Y[0], "o", color="#618abf")#marker_scale(R_EARTH)
mars_plot, = ax.plot(mars.X[0], mars.Y[0], "o", color="#f2663c") #marker_scale(R_MARS)

# Raketen
rocket_line = plt.plot(rocket.X, rocket.Y, ":")
rocket_plot, = ax.plot(rocket.X[0], rocket.Y[0], "p", color=(0,0,0,1), markersize=2)

#-----------------------------------------------------------------------------
# Animiere die Planeten
def animate(i):
    # Datenupdate
    #merkur_plot.set_data(merkur.X[i], merkur.Y[i])
    #venus_plot.set_data(venus.X[i], venus.Y[i])
    earth_plot.set_data(earth.X[i], earth.Y[i])
    mars_plot.set_data(mars.X[i], mars.Y[i])
    #rocket_line.set_data(rocket.X[:i], rocket.Y[:i])
    rocket_plot.set_data(rocket.X[i], rocket.Y[i])
    # Zeittextupdate
    #time_text.set_text(time_template % i)

#-----------------------------------------------------------------------------
# Starte die Simulation
if __name__ == '__main__':
    anim = animation.FuncAnimation(fig, animate, 
        frames=730, interval=1)
    print("Animation done.")
    #anim.save('docs/Abb/Abb_4.anim.gif', dpi=60, writer='imagemagick', fps=60)
    #print("Saving GIF done.")
    #anim.save('docs/Abb/Abb_4_anim.mp4', writer='ffmpeg', fps=60, bitrate=1800)
    #print("Saving MP4 done. Showing plot...")
    plt.show()
