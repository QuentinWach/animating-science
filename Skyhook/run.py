# Module
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Abschusszeit
T = 0
# Massen der Körper [kg]
M_SUN = 0
M_EARTH = 0
M_MARS = 0 
M_ROC = 0
# Umlaufzeiten [Tage]
UT_SUN = 1
UT_EARTH = 365
UT_MARS = 730
# Abstände zur Sonne [10³km]
D_SUN = 0
D_EARTH = 496000000
D_MARS = 1.5 * D_EARTH
# Radien der Körper [10³km]
R_SUN =     69634200
R_EARTH =   6.371001
R_MARS =    3.389500
R_ROC =            1

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
earth = Planet(M_EARTH, UT_EARTH, D_EARTH, R_EARTH)
mars = Planet(M_MARS, UT_MARS, D_MARS, R_MARS)


# Sammle die Positionen der Planeten im Zeitverlauf
TIME = 730 #UT_EARTH * UT_MARS #for perfect looping
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
# Plotdesign
plt.style.use("default")
plt.style.use("seaborn-dark")
plt.style.use("grayscale")
fig, ax = plt.subplots(figsize=(7,7), dpi=120)
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
plt.plot(0,0, "o", color="#ffbd5b", markersize=marker_scale(R_SUN))
# Erde
plt.plot(earth.X, earth.Y) # Bahn
earth_plot, = ax.plot(earth.X[0], earth.Y[0], "o", color="#618abf", markersize=marker_scale(R_EARTH))
# Mars
plt.plot(mars.X, mars.Y) # Bahn
mars_plot, = ax.plot(mars.X[0], mars.Y[0], "o", color="#f2663c", markersize=marker_scale(R_MARS))

#-----------------------------------------------------------------------------
# Animiere die Planeten
def animate(i):
    # Datenupdate
    earth_plot.set_data(earth.X[i], earth.Y[i])
    mars_plot.set_data(mars.X[i], mars.Y[i])
    # Zeittextupdate
    #time_text.set_text(time_template % i)

    return earth_plot, mars_plot,

#-----------------------------------------------------------------------------
# Starte die Simulation
if __name__ == '__main__':
    anim = animation.FuncAnimation(fig, animate, 
        frames=730, interval=1)
    print("Animation done. Saving...")
    #anim.save('docs/Abb/Abb.1.anim.gif', dpi=60, writer='imagemagick', fps=60)
    #print("Saving GIF done.")
    #anim.save('docs/Abb/Abb.2.anim.mp4', writer='ffmpeg', fps=60, bitrate=1800)
    #print("Saving MP4 done. Showing plot...")
plt.show()

