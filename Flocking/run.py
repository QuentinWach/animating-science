import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import progressbar
import movie

# hyper parameters
np.random.seed(12)

BIRD_COUNT = 750
VEL = 0.03
RAD = 0.06
RANDOMNESS = 0.045

STEPS = 25 * 5

# define the individual bird
class Bird:
    def __init__(self, x, y, a_init, v, r, alpha):
        self.X = x
        self.Y = y
        self.A = a_init
        self.V = v
        self.R = r
        self.ALPHA = alpha

    # boundary teleport
    def teleport(self):
        if self.X >= 1.0:
            self.X = self.X - 2
        if self.X <= -1.0:
            self.X = self.X + 2 
        if self.Y >= 1.0:
            self.Y = self.Y - 2
        if self.Y <= -1.0:
            self.Y = self.Y + 2 

    # introduce randomness
    def mad(self):
        # angle
        self.A = self.A + ((np.random.rand()*2-1) * 360) * RANDOMNESS
        if self.A >= 360:
            self.A = self.A - 360

        # vel
        self.V = self.V + ((np.random.rand()*2-1) * 0.02) * RANDOMNESS

    # normal movement
    def move(self):
        self.X = self.X + self.V * np.sin(np.radians(self.A))
        self.Y = self.Y + self.V * np.cos(np.radians(self.A))

# measure ho flocky the birds are
def flockiness(RES=1):
    # mean bird number for each area
    mean = BIRD_COUNT // RES 

    # actual bird number for each area
    mDensities = []
    for B in BIRDS:
        for x in range(RES):
            for y in range(RES):
                N = 0
                if B.X >= x-1 and B.X <= x+1:
                    if B.Y >= y and B.Y <= y+1:
                        N += 1
                mDensities.append(N)

    return mean, mDensities

# initialize the flock
BIRDS = []
def randomInit(BIRD_COUNT):
    for n in range(BIRD_COUNT):
        x = np.random.rand() * 2 - 1
        y = np.random.rand() * 2 - 1 
        a = np.random.rand()*360
        v = VEL #0.02
        r = RAD #0.06
        alpha = 90
        BIRDS.append(Bird(x,y,a,v,r,alpha))

def main(BIRD_COUNT, STEPS):
    # initialize the birds
    randomInit(BIRD_COUNT)

    Ds = []

    # run the flocking simulation
    for step in progressbar.progressbar(range(STEPS)):

        # create figure
        fig = plt.figure(figsize=(10,4),dpi=200)

        # update
        X = []; Y = []
        for Bird in BIRDS:
            Bird.teleport()
            Bird.mad()

            for B in BIRDS:
                if Bird != B:
                    if np.sqrt((Bird.X - B.X)**2 + (Bird.Y - B.Y)**2) <= Bird.R:
                        Bird.A = 0.85 * Bird.A + 0.15 * B.A 
            Bird.move()
            X.append(Bird.X)
            Y.append(Bird.Y)

        # measure the densities
        mean, mDensities = flockiness()
        R = np.random.normal(60,4*(1+step*0.006))
        Ds.append(R)


        matplotlib.style.use("ggplot")
        # SIMULATION
        ax1 = plt.subplot2grid((4,10),(0,0), colspan=4, rowspan=4)
        plt.xticks([])
        plt.yticks([])
        plt.axis([-1.0,1.0,-1.0,1.0])
        plt.scatter(X,Y, s=4, color="black")


        # SIMULATION
        #ax1 = plt.subplot2grid((4,10),(0,0), colspan=4, rowspan=4)
        #ax1.set_xticks([])
        #ax1.set_yticks([])
        #ax1.axis([-1.0,1.0,-1.0,1.0])
        #ax1.scatter(X,Y, s=4, color="black")

        #matplotlib.style.use("classic")
        
        # MEASUREMENT
        #ax2 = plt.subplot2grid((4,10),(0,4), colspan=6, rowspan=4)
        #ax2.plot(np.arange(0,STEPS+1),60 * np.ones(STEPS+1),"--", color="black")
        #ax2.plot(np.arange(0,step+1), np.asarray(Ds), color="crimson",alpha=0.8, lw=2.5)
        #ax2.set_xlim(0,STEPS)
        #ax2.set_ylim(0,120)

        # render
        plt.tight_layout()
        plt.savefig("./imgs/" + str(step) + ".png", bbox_inches="tight")
        plt.close()



movie.delImgs()
#main(BIRD_COUNT, STEPS)
#movie.createVideo("single")