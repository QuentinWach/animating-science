# GALAXIENKOLLISION, 13. Dezember 2019
"""
[X] 2D - Brute Force mit einfacher linearer Näherung der Newtonschen Grav pro Zeitschritt
[ ] 2D - Barnes-Hut Algorithmus
[ ] 3D 
Es wird angenommen, dass die Sterne im Vergleich zum Massezentrum des Clusters
eine derart kleine Masse haben, dass sie keinen gravitativen Einfluss ausüben.
"""
import matplotlib.pyplot as plt
import numpy as np
import math as m
import time

# TODO: LET BODIES MERGE WHEN THE YMOVE CLOSE TO EACH OTHER SO THAT
# THEY DONT ALWAYS FLY SO FAST AWAY THAT IT SEEMS THEY POPPED OUT OF EXISTENCE.

class BlackHole:
    """
    # Schwarzes Loch
    Es besitzt eine 
        + Masse
        + Position
        + Geschwindigkeitsvektor
    """
    # init den Körper an einem bestimmeten Punkt,
    # mit gegebener Masse und Geschwindigkeit
    def __init__(self,mass, xpos, ypos, xvel, yvel, radius):
        self.MASSE = mass
        self.XPOS = [xpos]
        self.YPOS = [ypos]
        self.XVEL = xvel
        self.YVEL = yvel
        self.RADIUS = radius

BHs = []
def randomInit(NUMBER):
    for n in range(NUMBER):
        BHs.append(BlackHole(1,np.random.rand(), np.random.rand(),0,0,0.2))

def PhiInit(NUMBER):
    phi = m.radians(137.508)
    for n in range(NUMBER):
        x = m.sqrt(n)*4*np.pi/NUMBER * np.cos(n * phi)
        y = m.sqrt(n)*4*np.pi/NUMBER * np.sin(n * phi)
        BHs.append(BlackHole(1,x,y,0,0,0.2))

def sim(TIME,STEPSIZE):
    for t in range(TIME):
            start = time.time()
            for BH1 in BHs:
                x_step = 0
                y_step = 0 
                for BH2 in BHs: 
                    if BH1 != BH2:
                        # calculate position vectors
                        x_dist = BH1.XPOS[t] - BH2.XPOS[t]
                        y_dist = BH1.YPOS[t] - BH2.YPOS[t]
                        r = np.sqrt(x_dist**2 + y_dist**2)
                        # check wether the bodys are so close to another they merge
                        #if r <= BH2.RADIUS:
                        if not r <= 0.05: 
                            # compute grav step
                            x_g_step = - BH1.MASSE * x_dist / r**3 
                            y_g_step = - BH1.MASSE * y_dist / r**3 
                            # compute total step
                            x_step +=  x_g_step
                            y_step +=  y_g_step
                # append the new position
                BH1.XPOS.append(BH1.XPOS[t]+ STEPSIZE*x_step)
                BH1.YPOS.append(BH1.YPOS[t]+ STEPSIZE*y_step)
                # update velocity
                BH1.XVEL = x_step + BH1.XVEL
                BH1.YVEL = y_step + BH1.YVEL
            stop = time.time()
            print("=======================================================================")
            print("CALCULATING TIMESTEP... " + str(t) + " | " + str(TIME))
            print("ESTIMATED REMAINING TIME: " + str(int(abs(start - stop)*(TIME-t))) + "s")


def statplot(TIME):
    for t in range(TIME):
        plt.style.use("default")
        fig = plt.figure(figsize=(3,3), dpi=150)

        ax = plt.gca()
        fig.add_axes(ax)
        ax.set_autoscale_on(False)
        ax.set_axis_off()
        ax.grid()

        plt.xticks([])
        plt.yticks([])
        plt.axis([-1,1,-1,1])
        # plotting
        for B in BHs:
            #plt.plot(B.XPOS[:t],B.YPOS[:t], "--", linewidth=0.125, color="grey")
            plt.plot(B.XPOS[t],B.YPOS[t], "o", color="black", markersize=0.3)

        plt.savefig("./Abb_" + str(t) + ".png", bbox_inches="tight")
        print("SAVED IMG " + str(t))
        plt.close()

####################################################
TIME = 60             # 60
STEPSIZE = 0.00001    # 0.000005

# simulate the masses
#randomInit(1500)     # 1500
PhiInit(300)

sim(TIME,STEPSIZE)
# plot all trajectories
statplot(TIME)


