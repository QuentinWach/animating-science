import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

x1 =-1.
y1 = 0.1
x1_v = 0
y1_v = 0

x2 = 1.
y2 = 0.1
x2_v = 0
y2_v = 0

TIME = 1000


class Ladung:
    """
    [X] Ladung und Position
    [ ] elektrisches Feld
    [ ] Geschwindigkeit
    [ ] erzeugtes Magnetfeld durch Geschwindigkeit
    """
    def __init__(self, q, x, y, vx, vy):
        self.q = q
        self.x = [x]
        self.y = [y]
        self.vx = [vx]
        self.vy = [vy]

    def status(self):
        print(self.q)
        print(self.x)
        print(self.y)

# Ladungskonfiguration
L = [Ladung(-1,x1,y1, x1_v, y1_v),
     Ladung(1,x2,y2, x2_v, y2_v)]

# Neue Positionen durch Coulomb Kraft
for t in range(TIME-1):


    L[0].x.append( ((((L[0].q * L[1].q) * (L[0].x[t] - L[1].x[t])) / np.sqrt(L[0].x[t] - L[1].x[t])**3) * 0.5) + L[0].vx)
    L[1].x.append( ((((L[0].q * L[1].q) * (L[1].x[t] - L[0].x[t])) / np.sqrt(L[1].x[t] - L[0].x[t])**3) * 0.5) + L[0].vy)
    L[0].y.append( ((((L[0].q * L[1].q) * (L[0].y[t] - L[1].y[t])) / np.sqrt(L[0].x[t] - L[1].x[t])**3) * 0.5) + L[1].vx)
    L[1].y.append( ((((L[0].q * L[1].q) * (L[1].y[t] - L[0].y[t])) / np.sqrt(L[1].y[t] - L[0].y[t])**3) * 0.5) + L[1].vy)

    #L[1].x.append(L[1].x[0])
    #L[1].y.append(L[1].y[0])


# Plotte die Bahnen und initialisiere die Animation (Plotdesign)
#plt.style.use("default")
#plt.style.use("seaborn-dark")
#plt.style.use("grayscale")
fig, ax = plt.subplots(figsize=(8,8),dpi=120) #figsize=(7,7)
fig.patch.set_facecolor('white')
fig.canvas.set_window_title('Elektronen')
#plt.xticks([])
#plt.yticks([])

#l1, = ax.plot(L[0].x[0],L[0].y[0],"o")
#l2, = ax.plot(L[1].x[0],L[1].y[0],"o")

print(L[0].x)
plt.plot(L[0].x, L[0].y, "--")
plt.show()
"""
# Animiere die Elektronenbewegungen
def animate(i):
    # Datenupdate
    l1.set_data(L[0].x[i], L[0].y[i])
    l2.set_data(L[1].x[i], L[1].y[i])

#-----------------------------------------------------------------------------
# Starte die Simulation
anim = animation.FuncAnimation(fig, animate, frames=TIME, interval=1)
print("Animation done.")
#anim.save('docs/Abb/Abb_4.anim.gif', dpi=60, writer='imagemagick', fps=60)
#print("Saving GIF done.")
#anim.save('docs/Abb/Abb_4_anim.mp4', writer='ffmpeg', fps=60, bitrate=1800)
#print("Saving MP4 done. Showing plot...")
plt.show()
"""




