# GALAXIENKOLLISION, 13. Dezember 2019
import matplotlib.pyplot as plt
import numpy as np
import math as m
import time
import movie

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
        self.MASSE = mass * 100000
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

STs = []
BHs = []
def randomInit(NUMBER, TYPE="BHs"):
    for n in range(NUMBER):
        weight = (NUMBER / 300)**2
        x = np.random.rand() * 2 -1
        y = np.random.rand() * 2 -1
        xv = (np.random.rand() * 2 -1) * 10
        yv = (np.random.rand() * 2 -1) * 10
        if TYPE == "BHs":
            BHs.append(BlackHole(weight,x,y,xv,yv,0.2))
        if TYPE == "STs":
            STs.append(Star(weight,x,y,xv,yv,0.2))

def phiInit(NUMBER, TYPE="BHs"):
    phi = m.radians(137.508)
    weight = (NUMBER / 300)**2
    for n in range(NUMBER*2):
        if np.random.rand() >= 0.5:
            x = m.sqrt(n)*11*np.pi/NUMBER * np.cos(n * phi)
            y = m.sqrt(n)*11*np.pi/NUMBER * np.sin(n * phi)
            r = m.sqrt(x**2 + y**2)
            vx = x/(r+0.1) * 0
            vy = y/(r+0.1) * 0
            if TYPE == "BHs":
                BHs.append(BlackHole(weight,x,y,vx,vy,0.2))
            if TYPE == "STs":
                STs.append(Star(weight,x,y,vx,vy,0.2))

def NebulaInit(NUMBER, X, Y, XV, YV):
    # initilaize a number of black holes each with a certain number of 
    # rotating stars around them
    n=NUMBER
    weight = (NUMBER / 300)**2 * 0.3
    a=0.5 * 0.5
    b=0.6 * 0.5
    th=np.random.randn(n)
    x=a*np.exp(b*th)*np.cos(th) + X
    y=a*np.exp(b*th)*np.sin(th) + Y
    x1=a*np.exp(b*(th))*np.cos(th+np.pi) + X
    y1=a*np.exp(b*(th))*np.sin(th+np.pi) + Y

    sx=np.random.normal(0, a*0.25, n)
    sy=np.random.normal(0, a*0.25, n)

    BHs.append(BlackHole(0.002, X, Y, XV, YV, 0.2))

    for e in range(NUMBER):
        # Abstände zum Zentrum
        r1 = np.sqrt((x[e]+sy[e])**2 + (y[e]+sx[e])**2)
        r2 = np.sqrt((x1[e]+sx[e])**2 + (y1[e]+sy[e])**2)
        # Geschwindigkeiten (Beweung im Uhrzeigersinn)
        v_max = 10000 * 0.1   #0.1
        vx1 = -(v_max / (1+r1)) * np.cos(y[e]+sx[e]) - XV
        vy1 = -(v_max / (1+r1)) * np.sin(x[e]+sy[e]) - YV
        vx2 = (v_max / (1+r2)) * np.sin(y1[e]+sx[e]) + XV
        vy2 = (v_max / (1 + r2)) * np.cos(x1[e]+sy[e]) + YV
        # Schaffe die schweren Körper
        STs.append(Star(weight,x[e]+sy[e],y[e]+sx[e],vx1,vy1,0.2))
        STs.append(Star(weight,x1[e]+sx[e],y1[e]+sy[e],vx2,vy2,0.2))

def simOpen(TIME,STEPSIZE):
    for t in range(TIME):
            start = time.time()
            # LÖCHER
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
                # add its current velocity
                x_step += BH1.XVEL
                y_step += BH1.YVEL
                # append the new position
                BH1.XPOS.append(BH1.XPOS[t]+ STEPSIZE*x_step)
                BH1.YPOS.append(BH1.YPOS[t]+ STEPSIZE*y_step)
                # update velocity
                BH1.XVEL = x_step
                BH1.YVEL = y_step

            # STERNE
            for ST in STs:
                x_step = 0
                y_step = 0
                for BH in BHs:
                    # calculate position vectors
                    x_dist = ST.XPOS[t] - BH.XPOS[t]
                    y_dist = ST.YPOS[t] - BH.YPOS[t]
                    r = np.sqrt(GRAV_SMOOTHING**2 + x_dist**2 + y_dist**2)
                    # compute grav step
                    x_g_step = - BH.MASSE * x_dist / r**3 
                    y_g_step = - BH.MASSE * y_dist / r**3 
                    # compute total step
                    x_step +=  x_g_step 
                    y_step +=  y_g_step 
                # add its current velocity
                x_step += ST.XVEL
                y_step += ST.YVEL
                # append the new position
                ST.XPOS.append(ST.XPOS[t]+ STEPSIZE*x_step)
                ST.YPOS.append(ST.YPOS[t]+ STEPSIZE*y_step)
                # update velocity
                ST.XVEL = x_step
                ST.YVEL = y_step


            stop = time.time()
            print("=======================================================================")
            print("CALCULATING TIMESTEP... " + str(t) + " | " + str(TIME))
            print("ESTIMATED REMAINING TIME: " + str(int(abs(start - stop)*(TIME-t))) + "s")

def statplot(TIME):
    for t in range(TIME):
        start = time.time()
        plt.style.use("default")
        fig, ax = plt.subplots(1, figsize=(3,3), dpi=300)

        c = 0
        for S in STs:
            #if c % 5 == 0:
            #    plt.plot(S.XPOS[:t+1],S.YPOS[:t+1], "--", linewidth=0.1, color="white")
            plt.plot(S.XPOS[t],S.YPOS[t], "o", color="white", markersize=0.05)
            c += 1

        for B in BHs:
            plt.plot(B.XPOS[:t+1],B.YPOS[:t+1], "--", linewidth=0.1, color="r")
            plt.plot(B.XPOS[t],B.YPOS[t], "o", color="r", markersize=2)

        plt.xticks([])
        plt.yticks([])
        plt.axis([-2.,2.,-2.,2.])
        ax.set_facecolor('black')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)

        plt.savefig("./images/Abb_" + str(t) + ".png", bbox_inches="tight", facecolor='black')
        stop = time.time()
        print("=======================================================================")
        print("CALCULATING TIMESTEP... " + str(t) + " | " + str(TIME))
        print("ESTIMATED REMAINING TIME: " + str(int(abs(start - stop)*(TIME-t))) + "s")        
        print("SAVED IMG " + str(t))
        plt.close()

def hexplot(TIME):
    for t in range(TIME):
        start = time.time()
        plt.style.use("default")
        fig, ax = plt.subplots(1, figsize=(3,3), dpi=300)

        x = []
        y = []
        for S in STs:
            x.append(S.XPOS[t])
            y.append(S.YPOS[t])
        plt.hexbin(x, y, gridsize=175, linewidths=0.1, bins="log", cmap='inferno', vmin=1, vmax=60, extent=(-1.2,1.2,-1.2,1.2))
        
        for B in BHs:
            plt.plot(B.XPOS[:t+1],B.YPOS[:t+1], "--", linewidth=0.3, color="white")
            plt.plot(B.XPOS[t],B.YPOS[t], "o", color="white", markersize=1.3)


        plt.xticks([])
        plt.yticks([])
        plt.axis([-1.15,1.15,-1.15,1.15])
        ax.set_facecolor('black')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)

        plt.savefig("./images/Abb_" + str(t) + ".png", bbox_inches="tight", facecolor='black')
        stop = time.time()
        print("=======================================================================")
        print("CALCULATING TIMESTEP... " + str(t) + " | " + str(TIME))
        print("ESTIMATED REMAINING TIME: " + str(int(abs(start - stop)*(TIME-t))) + "s")        
        print("SAVED IMG " + str(t))
        plt.close()




####################################################
np.random.seed(42)
BLACK_HOLES = 2
STARS = 10000 #5000
TIME = 24 * 6         # 60
STEPSIZE = 0.000001 * 1200 / BLACK_HOLES * 0.1  # 4
GRAV_SMOOTHING = 0.2

"""
# initialize system
#randomInit(BLACK_HOLES, TYPE="BHs"); randomInit(STARS, TYPE="STs")     # 1500
#phiInit(PARTICLES)
NebulaInit(STARS, -0.75, 0, 0, 605)
NebulaInit(STARS, 0.75, 0, 0, -605)
# simulate the masses
simOpen(TIME,STEPSIZE)
# plot all trajectories
#statplot(TIME)
hexplot(TIME)
"""
# create movie file
movie.createVideo("nebulaY3")
####################################################
