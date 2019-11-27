# Theoretische Physik
# Vis eines Magnetfeldes
import numpy as np
import matplotlib.pyplot as plt

# Konstanten
eps = 1
mü = 1
R = 4
I = 1

# Raster
X,Y = np.meshgrid(np.arange(-R,R,.002), np.arange(-R,R,.002))

# Vektorfeld
Bx = -Y * (mü * eps * I) / (np.pi * ((X**2 + Y**2)))
By =  X * (mü * eps * I) / (np.pi * (X**2 +Y**2))

B = 1/(X**2+Y**2)**0.5 + 0.65

plt.style.use("default")
plt.style.use("seaborn-dark")
plt.style.use("grayscale")

fig = plt.figure(figsize=(7,7), dpi=250)
fig.patch.set_facecolor("white")
ax = plt.Axes(fig, [0., 0., 1., 1.])
ax.set_axis_off()
ax.grid()
fig.add_axes(ax)
plt.xticks([])
plt.yticks([])

# Plotten der Feldlinien
plt.streamplot(X,Y,Bx,By, color = (0,0.5,0.7,1), cmap="inferno", density=2, linewidth=B, arrowsize=0.8)

# Plotten der Kreisplattenform
t = np.arange(301)
plt.plot(4*np.cos(2*np.pi/300 * t), 4*np.sin(2*np.pi/300 * t), lw=3)
plt.plot(4.7*np.cos(2*np.pi/300 * t), 4.7*np.sin(2*np.pi/300 * t), lw=64, color="white")

# Save
plt.savefig("./Abb_1.png")
print("SAVED STREAMPLOT.")