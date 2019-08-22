from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from matplotlib.animation import Animation
import numpy as np
from math import *


t = 0.1
omega = 2.
x = np.arange(-5,5,0.01) 
y = np.arange(-5,5,0.01)
x,y = np.meshgrid(x,y)
z = 1.0
r = np.sqrt(x**2 + y**2 + z**2)
p1 = 2.
p2 = -2.
p3 = 0.
c = 1
epsilon = 8.85418782 * 10**(0)
Skalierung = omega**3 / (4 * np.pi * epsilon * c**3)

def E(t):

    Welle = np.cos(omega*((r/c)-t*2*np.pi))
    E = Skalierung *  Welle * np.sqrt(c**2*(-p1*x*z - p2*y*z + p3*(x**2 + y**2))**2/(omega**2*r**2) + (-p1 + z*(9*p1*x + 9*p2*y + 9*p3*z))**2*(c**6/(omega**6*r**6) - c**4/(omega**4*r**4)) + (c**2*(p1*(y**2 + z**2) - p2*x*y - p3*x*z)**2/(omega**2*r**2) + (-p1 + x*(9*p1*x + 9*p2*y + 9*p3*z))**2*(c**6/(omega**6*r**6) - c**4/(omega**4*r**4)))*(c**2*(-p1*x*y + p2*(x**2 + z**2) - p3*y*z)**2/(omega**2*r**2) + (-p1 + y*(9*p1*x + 9*p2*y + 9*p3*z))**2*(c**6/(omega**6*r**6) - c**4/(omega**4*r**4))))
    return E

# Zeige die Oberfläche
fig = plt.figure()
ax = fig.gca(projection='3d')
plt.style.use("default")
#p.style.use("seaborn-dark")
fig.patch.set_facecolor('white')
#ax.set_xlim([-10,10])
#ax.set_ylim([-10,10])
#ax.set_zlim([-4,4]*10**15)
#p.xticks([])
#p.yticks([])

#p.plot(y,Z)
#p.plot(x,Z)
surf = ax.plot_surface(x, y, E(0), cmap="Greys", linewidth=0, antialiased=True)





# Raketenbahn und Positionen
#rocket_line = plt.plot(rocket.X, rocket.Y, ":", lw=1)
#rocket_plot, = ax.plot(rocket.X[0], rocket.Y[0], "p", color=(0,0,0,1), markersize=4)

#-----------------------------------------------------------------------------
# Animiere die Planeten
def animate(i):
    # Datenupdate
    #rocket_line.set_data(rocket.X[:i], rocket.Y[:i])
    #rocket_plot.set_data(rocket.X[i], rocket.Y[i])
    surf.set_data(x, y, E(i))

TIME = 10
#anim = animation.FuncAnimation(fig, animate, frames=TIME, interval=1)
print("Animation done.")
#anim.save('docs/Abb/Abb_4.anim.gif', dpi=60, writer='imagemagick', fps=60)
#print("Saving GIF done.")
#anim.save('docs/Abb/Abb_4_anim.mp4', writer='ffmpeg', fps=60, bitrate=1800)
#print("Saving MP4 done. Showing plot...")
plt.show()