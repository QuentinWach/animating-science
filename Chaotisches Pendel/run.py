# CHAOTISCHES DOPPELPENDEL
# ========================
# Theoretische Physik
# Quentin Wach, 14. November 2018

from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation

# Parameter
dt = 0.03 # Zeitauflösung (bzw. t_res)
t = np.arange(0.0, 50, dt) # Zeitintervall [s]
G = 9.8   # Erdbeschleunigung [m/s^2]
L1 = 1.0  # Länge des Pendel 1 [m]
L2 = 1.0  # Länge des Pendel 2 [m]
M1 = 1.0  # Masse des Pendel 1 [kg]
M2 = 1.0  # Masse des Pendel 2 [kg]

th1 = 180.0 # Anfangswinkel 1 [°]
th2 = 181.0 # Anfangswinkel 2 [°]
w1 = 0.0 # Anfangsgeschwindigkeit 1 [°/s]
w2 = 0.0 # Anfangsgeschwindigkeit 2 [°/s]

# Anfangsbedingung
state = np.radians([th1, w1, th2, w2])

# Bilden des DGL Systems
def derivs(state, t):

    dydx = np.zeros_like(state)
    dydx[0] = state[1]

    del_ = state[2] - state[0]
    den1 = (M1 + M2)*L1 - M2*L1*cos(del_)*cos(del_)
    dydx[1] = (M2*L1*state[1]*state[1]*sin(del_)*cos(del_) +
               M2*G*sin(state[2])*cos(del_) +
               M2*L2*state[3]*state[3]*sin(del_) -
               (M1 + M2)*G*sin(state[0]))/den1

    dydx[2] = state[3]

    den2 = (L2/L1)*den1
    dydx[3] = (-M2*L2*state[3]*state[3]*sin(del_)*cos(del_) +
               (M1 + M2)*G*sin(state[0])*cos(del_) -
               (M1 + M2)*L1*state[1]*state[1]*sin(del_) -
               (M1 + M2)*G*sin(state[2]))/den2

    return dydx

# Integriere das System der gewöhnlichen DGLs und gewinne die Koordinaten
y = integrate.odeint(derivs, state, t)
x1 = L1*sin(y[:, 0])
y1 = -L1*cos(y[:, 0])
x2 = L2*sin(y[:, 2]) + x1
y2 = -L2*cos(y[:, 2]) + y1

# Plotte die Figur
# Plotdesign
plt.style.use("default")
plt.style.use("seaborn-dark")
plt.style.use("grayscale")
fig = plt.figure(num=None, figsize=(3, 3), dpi=200, facecolor='w', edgecolor='k')
fig = plt.gcf()
fig.canvas.set_window_title('Chaotisches Doppelpendel')
fig.patch.set_facecolor('white')
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-2.1, 2.1), ylim=(-2.1, 2.1))
ax.grid()
plt.xticks([])
plt.yticks([])

# Achsenbeschriftungen
#plt.xlabel("x-Achse / m")
#plt.ylabel("y-Achse / m")

# Zeige die moementane Ausrichtung des Pendels
line, = ax.plot([], [], 'o-', color=(0,0,0,1), lw=1, zorder = 5)

# Zeige die vergangenen Punkte
#pastx = []
#pasty = []
#dots, = ax.plot(pastx, pasty, ".-", color=(0,0,0,0.25), lw=2, zorder = 3)

# Zeige die momentane Zeit
#time_template = 'Zeit = %.1fs'
#time_text = ax.text(0.80, .95, '', bbox=dict(facecolor='white', alpha=0.8), transform=ax.transAxes)

def init():
    line.set_data([], [])
    #dots.set_data([], [])
    #time_text.set_text('')
    return line, dots, time_text

def animate(i):
    # Koordinaten der drei Punkte
    thisx = [0, x1[i], x2[i]]
    thisy = [0, y1[i], y2[i]]

    # Drucke die Koordinaten im Terminal
    print("x(" + str(i) + ") = " + str(thisx))
    print("y(" + str(i) + ") = " + str(thisy))
    """
    # Merke vergangene Koordinaten
    if i <= 1000:
      pastx.append(thisx[2]); pasty.append(thisy[2])
    else:
      pastx.pop(0); pasty.pop(0)
      pastx.append(thisx[2]); pasty.append(thisy[2])
    """
    # Datenupdate
    line.set_data(thisx, thisy)
    #dots.set_data(pastx, pasty)

    # Zeittextupdate
    #time_text.set_text(time_template % (i*dt))

    return line, #dots, time_text

anim = animation.FuncAnimation(fig, animate, frames=np.arange(0, len(y), 1), interval=15)
#anim.save('pendel.gif', dpi=80, writer='imagemagick') # Zum speichern der Animation als .gif
anim.save('pendel.mp4', writer='ffmpeg', fps=60, bitrate=1800)

plt.show()
