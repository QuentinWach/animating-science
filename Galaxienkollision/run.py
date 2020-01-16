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
import movie

# TODO: LET BODIES MERGE WHEN THE YMOVE CLOSE TO EACH OTHER SO THAT
#       THEY DONT ALWAYS FLY SO FAST AWAY THAT IT SEEMS THEY POPPED OUT OF EXISTENCE.

class BlackHole:
    """
    # Schwarzes Loch. Interargiert nur mit schwarzen Löchern
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

class Star:
    """
    # Stern. Interagiert nur mit Sternen
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
        x = np.random.rand() * 2 -1
        y = np.random.rand() * 2 -1
        xv = (np.random.rand() * 2 -1) * 0 #10
        yv = (np.random.rand() * 2 -1) * 0 #10
        BHs.append(BlackHole(1,x,y,xv,yv,0.2))

def phiInit(NUMBER):
    phi = m.radians(137.508)
    for n in range(NUMBER*2):
        if np.random.rand() >= 0.5:
            x = m.sqrt(n)*4*np.pi/NUMBER * np.cos(n * phi)
            y = m.sqrt(n)*4*np.pi/NUMBER * np.sin(n * phi)
            BHs.append(BlackHole(1,x,y,0,0,0.2))

def GalaxieInit(BH_NUMBER, ST_NUMBER):
    # initilaize a number of black holes each with a certain number of 
    # rotating stars around them
    n=1000
    a=0.5
    b=0.6
    th=np.random.randn(n)
    x=a*np.exp(b*th)*np.cos(th)
    y=a*np.exp(b*th)*np.sin(th)
    x1=a*np.exp(b*(th))*np.cos(th+np.pi)
    y1=a*np.exp(b*(th))*np.sin(th+np.pi)

    sx=np.random.normal(0, a*0.25, n)
    sy=np.random.normal(0, a*0.25, n)

    plt.style.use("default")
    fig, ax = plt.subplots(1, dpi=300)

    plt.plot(x+sy,y+sx,".", markersize=0.3, color="white")
    plt.plot(x1+sx, y1+sy,".", markersize=0.3, color="white")

    plt.xticks([])
    plt.yticks([])
    ax.set_facecolor('black')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    plt.savefig("./AbbG" + ".png", bbox_inches="tight", facecolor='black')
    print("SAVED IMG")
    plt.close()

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
                        r = np.sqrt(GRAV_SMOOTHING**2 + x_dist**2 + y_dist**2)

                        # compute grav step
                        x_g_step = - BH2.MASSE * x_dist / r**3 
                        y_g_step = - BH2.MASSE * y_dist / r**3 
                        # compute total step
                        x_step +=  x_g_step 
                        y_step +=  y_g_step 
                x_step += BH1.XVEL
                y_step += BH1.YVEL
                # append the new position with added own velocity
                BH1.XPOS.append(BH1.XPOS[t]+ STEPSIZE*x_step)
                BH1.YPOS.append(BH1.YPOS[t]+ STEPSIZE*y_step)
                # update velocity
                BH1.XVEL = x_step
                BH1.YVEL = y_step

            stop = time.time()
            print("=======================================================================")
            print("CALCULATING TIMESTEP... " + str(t) + " | " + str(TIME))
            print("ESTIMATED REMAINING TIME: " + str(int(abs(start - stop)*(TIME-t))) + "s")

def speedColor(POScurrent, POSbefore):
    """
    Returns a color on a spectrum given the velocity of the particle.
    """
    pass

def densityColor():
    """
    Returns a color for a given particle estimated by density of surrounding particles.
    """
    pass

def statplot(TIME):
    for t in range(TIME):
        plt.style.use("default")
        #fig = plt.figure(figsize=(3,3), dpi=150)
        fig, ax = plt.subplots(1, figsize=(3,3), dpi=300)

        ## plotting
        c = 0
        for B in BHs:
            if c % 10 == 0:
                plt.plot(B.XPOS[:t+1],B.YPOS[:t+1], "--", linewidth=0.15, color="c")
            plt.plot(B.XPOS[t],B.YPOS[t], "o", color="white", markersize=0.33)
            c += 1

        plt.xticks([])
        plt.yticks([])
        #plt.axis([-1.,1.,-1.,1.])
        plt.axis([-2.,2.,-2.,2.])
        ax.set_facecolor('black')
        #ax.grid(False)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)


        plt.savefig("./images/Abb_" + str(t) + ".png", bbox_inches="tight", facecolor='black')
        print("SAVED IMG " + str(t))
        plt.close()

####################################################
np.random.seed(42)
TIME = 30           # 60
STEPSIZE = 0.000001 * 4   # 0.000005
GRAV_SMOOTHING = 0.1

# initialize system
randomInit(300)     # 1500
#phiInit(300)
# simulate the masses
sim(TIME,STEPSIZE)
# plot all trajectories
statplot(TIME)
# create movie file
movie.createVideo("test_vel_off10")
####################################################
