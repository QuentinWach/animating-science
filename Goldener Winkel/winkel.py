import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import math as m

plt.style.use("default")
plt.style.use("seaborn-dark")
plt.style.use("grayscale")
fig, ax = plt.subplots(figsize=(8,8),dpi=120)
fig.patch.set_facecolor('white')
plt.xticks([])
plt.yticks([])
#-------------

swinkel = m.radians(135)
phi = m.radians(137.508)

X = []
Y = []
points = 100
def gen(winkel):
    for p in range(points):
        X.append(m.sqrt(p) * np.cos(p * winkel))
        Y.append(m.sqrt(p) * np.sin(p * winkel))

# Startbild
gen(swinkel)
abb, = ax.plot(X,Y, "o")

# Animationsupdate
def animate(i):
    winkel = (i*0.0002 +1) * swinkel
    A = []
    B = []
    for p in range(points):
        A.append(m.sqrt(p) * np.cos(p * winkel))
        B.append(m.sqrt(p) * np.sin(p * winkel))
    abb.set_data(A,B)
    print(str(i) + " ---- " + str(m.degrees(winkel)))

# Animation des Bereichs um Phi
anim = animation.FuncAnimation(fig, animate, frames=180, interval=50)
#anim.save('gold.gif', dpi=80, writer='imagemagick') # Zum speichern der Animation als .gif
#anim.save('gold.mp4', writer='ffmpeg', fps=50, bitrate=1800)
plt.show()