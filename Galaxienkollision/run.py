# GALAXIENKOLLISION, 13. Dezember 2019
import matplotlib.pyplot as plt
# for LaTeX font
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)
import numpy as np
import math as m
import time
import progressbar
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
        self.MASSE = mass * 10
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
#---------------------------------------------------
STs = []
BHs = []
#---------------------------------------------------
def randomInit(NUMBER, TYPE="BHs"):
    for n in range(NUMBER):
        weight = 1#(NUMBER / 300)**2
        x = np.random.rand() * 2 -1
        y = np.random.rand() * 2 -1
        xv = (np.random.rand() * 2 -1) * 600
        yv = (np.random.rand() * 2 -1) * 600
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

def GalaxInit(NUMBER, X, Y, XV, YV):
    PHI  = m.radians(137.508)
    G = 4.75 # 4.75 <  < 5
    BHs.append(BlackHole(1, X, Y, XV, YV, 0.2))
    weight = (NUMBER / 300)**2 * 0.05
    for p in range(NUMBER):
        # füge x und y Koordinaten den Listen hinzu
        gauss = 1/(m.sqrt(2*np.pi))*m.exp(-4) # 5
        x =  gauss * m.sqrt(p) * np.cos(p * PHI) + (np.random.rand() * 2 - 1)*0.15  + X 
        y =  gauss * m.sqrt(p) * np.sin(p * PHI) + (np.random.rand() * 2 - 1)*0.15 + Y
        r = ((X-x)**2 + (Y-y)**2)**0.5
        # je größer der Abstand, desto schneller das Teilchen
        v = - m.sqrt(G*10**2 // r)
        vx = XV + v * np.cos((p) * PHI) - v**2 * np.sin((p) * PHI)
        vy = YV + v * np.sin((p) * PHI) + v**2 * np.cos((p) * PHI)
        # Schaffe die schweren Körper
        if r > 0.3:
            STs.append(Star(weight,x,y,vx,vy,0.2))
#---------------------------------------------------
def BHCenterOpenSim(TIME,STEPSIZE):
    for t in progressbar.progressbar(range(TIME)):
            #start = time.time()
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


            #stop = time.time()
            #print("=======================================================================")
            #print("CALCULATING TIMESTEP... " + str(t) + " | " + str(TIME))
            #print("ESTIMATED REMAINING TIME: " + str(int(abs(start - stop)*(TIME-t))) + "s")

def GeneralOpenSim(TIME,STEPSIZE):
    BODYs = STs + BHs
    for t in range(TIME):
            start = time.time()
            # LÖCHER
            for B1 in BODYs:
                x_step = 0
                y_step = 0
                for B2 in BODYs: 
                    if B1 != B2:
                        # calculate position vectors
                        x_dist = B1.XPOS[t] - B2.XPOS[t]
                        y_dist = B1.YPOS[t] - B2.YPOS[t]
                        r = np.sqrt(GRAV_SMOOTHING**2 + x_dist**2 + y_dist**2)
                        # compute grav step
                        x_g_step = - B2.MASSE * x_dist / r**3 
                        y_g_step = - B2.MASSE * y_dist / r**3 
                        # compute total step
                        x_step +=  x_g_step 
                        y_step +=  y_g_step 
                # add its current velocity
                x_step += B1.XVEL
                y_step += B1.YVEL
                # append the new position
                B1.XPOS.append(B1.XPOS[t]+ STEPSIZE*x_step)
                B1.YPOS.append(B1.YPOS[t]+ STEPSIZE*y_step)
                # update velocity
                B1.XVEL = x_step
                B1.YVEL = y_step

            stop = time.time()
            print("=======================================================================")
            print("CALCULATING TIMESTEP... " + str(t) + " | " + str(TIME))
            print("ESTIMATED REMAINING TIME: " + str(int(abs(start - stop)*(TIME-t))) + "s")
#---------------------------------------------------
def BHCenterStatplot(TIME):
    for t in range(TIME):
        start = time.time()
        plt.style.use("default")
        fig, ax = plt.subplots(1, figsize=(3,2), dpi=300)

        c = 0
        for S in STs:
            if c % 5 == 0:
                plt.plot(S.XPOS[:t+1],S.YPOS[:t+1], "--", linewidth=0.1, color="white")
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

def BHCenterHexplot(TIME):
    for t in progressbar.progressbar(range(TIME)):
        plt.style.use("default")
        fig, ax = plt.subplots(1, figsize=(3,3), dpi=300)

        x = []
        y = []
        c = 0
        for S in STs:
            if c % 100 == 0:
                if t > 6:
                    plt.plot(S.XPOS[t-6:t+1],S.YPOS[t-6:t+1], "--", linewidth=0.12, color="white")
                else:
                    plt.plot(S.XPOS[:t+1],S.YPOS[:t+1], "--", linewidth=0.12, color="white")
            c += 1
            x.append(S.XPOS[t])
            y.append(S.YPOS[t])
        plt.hexbin(x, y, gridsize=380, linewidths=0.01, bins="log", cmap='bone', vmin=1, vmax=16, extent=(-2.,2.,-2.,2.)) # inferno

        # inferno: Für Massendichte
        # gist_heat: Für Infrarot Strahlung

        for B in BHs:
            plt.plot(B.XPOS[:t+1],B.YPOS[:t+1], "--", linewidth=0.3, color="white")
            plt.plot(B.XPOS[t],B.YPOS[t], "o", color="white", markersize=1.3)


        plt.xticks([])
        plt.yticks([])
        plt.axis([-2.,2.,-2.,2])
        ax.set_facecolor('black')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)

        plt.savefig("./images/Abb_" + str(t) + ".png", bbox_inches="tight", facecolor='black')
        plt.close()


def GeneralStatplot(TIME):
    BODYs = STs + BHs
    for t in range(TIME):
        start = time.time()
        #plt.style.use("default")
        fig, ax = plt.subplots(1, figsize=(3,3), dpi=300)

        c = 0
        for B in BODYs:
            #if c % 5 == 0:
            plt.plot(B.XPOS[:t+1],B.YPOS[:t+1], "--", linewidth=0.2, color="white")
            plt.plot(B.XPOS[t],B.YPOS[t], "o", markersize=1.5)
            c += 1

        plt.xticks([])
        plt.yticks([])
        plt.axis([-2.,2.,-2.,2.])
        ax.set_facecolor('black')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)

        plt.text(-0.6,1.7,"SMOOTH GRAVITY IN A PLANE", color="white", size=7)
        plt.text(0.19,1.3,r"$\vec{F} = -G \cdot \frac{M_1 \cdot M_2}{r^2} \frac{\vec{r}}{r}$", color="white", size=8)
        plt.text(-1.03,-1.6,r"with $r=\sqrt{x^2 + y^2 + 0,1}$", color="white", size=8)
        plt.savefig("./images/Abb_" + str(t) + ".png", bbox_inches="tight", facecolor='black')
        stop = time.time()
        print("=======================================================================")
        print("CALCULATING TIMESTEP... " + str(t) + " | " + str(TIME))
        print("ESTIMATED REMAINING TIME: " + str(int(abs(start - stop)*(TIME-t))) + "s")        
        print("SAVED IMG " + str(t))
        plt.close()

def GeneralHexplot(TIME):
    BODYs = STs + BHs
    for t in range(TIME):
        start = time.time()
        plt.style.use("default")
        fig, ax = plt.subplots(1, figsize=(5,5), dpi=300)

        x = []
        y = []
        for B in BODYs:
            x.append(B.XPOS[t])
            y.append(B.YPOS[t])
        plt.hexbin(x, y, gridsize=175, linewidths=0.01, bins="log", cmap='inferno', vmin=0, vmax=15, extent=(-1.2,1.2,-1.2,1.2))

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

#---------------------------------------------------
np.random.seed(42)
BLACK_HOLES = 1
STARS = 25000
TIME = 2 #25 * 5
STEPSIZE = 0.00002 
GRAV_SMOOTHING = 0.1


# initialize system
#GalaxInit(STARS,-2.75, 0, 450, -50); GalaxInit(STARS, 0.75, 0, -150, 100)
#GalaxInit(STARS, 0, 0, 0, 0);
randomInit(6, "BHs")

# simulate
#BHCenterOpenSim(TIME,STEPSIZE)
GeneralOpenSim(TIME, STEPSIZE)
# plot positions and trajectories
#BHCenterHexplot(TIME)
GeneralStatplot(TIME)
# create movie file
#movie.createVideo("FUN3")