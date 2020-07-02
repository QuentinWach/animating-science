"""
Modul zur Visualisierung
------------------------
Ausbreitung eines Virus in einer Population als Zufallsprozess 
auf einem Graphen - Programmierprojekt zur COMAII, Teil 2
geschrieben von Quentin Wach, 18. Juni 2020
"""
import random
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from sim import Node, Virus
# zusätzliche Helfer-Module irrelevant für die Aufgabe
from alive_progress import alive_bar
import movie

def infect(PEOPLE, INFECTED):
    # returns a list of keys for the infected nodes
    infected = []
    for i in range(INFECTED):
        key = random.randrange(PEOPLE)+1 
        if key not in infected:
            infected.append(key)
        else:
            infect(PEOPLE, INFECTED-i)
    return infected

def SquareGraph(SIDE_LENGTH, INFECTED, START_TIME):
    # create a list of random coordinates in a dense square
    coords = []
    for x in range(SIDE_LENGTH):
        for y in range(SIDE_LENGTH):
            coords.append((x,y))
    # randomize coords
    random.shuffle(coords)
    # create node list with keys
    nodePrior = []
    for e in range(len(coords)):
        nodePrior.append([e, coords[e], -1])
    # find neighbor keys for each element and add them to nodePrior
    for n in nodePrior:
        base = n[1]
        neighs = []
        for a in [-1,0,1]:
            for b in [-1,0,1]:
                neighs.append((base[0] + a, base[1] + b))
                if a == b and a == 0:
                    neighs.pop()
        keys = []
        for nb in neighs:
            for node in nodePrior:
                if nb == node[1]:
                    if node[0] not in keys:
                        keys.append(node[0])
        n.append(sorted(keys))
    # create a list of keys for the infected nodes
    infected = infect(SIDE_LENGTH**2, INFECTED)
    # switch random nodes to be infected
    for k in infected:
        for n in nodePrior:
            if k == n[0]:
                n[2] = START_TIME
    # create the complete graph
    G = []
    for n in nodePrior:
        G.append(Node(n[0], n[1], n[2], n[3]))
    return G

class VisualizeVirus:
    def __init__(self, Virus):
        """
        VisualizeVirus uses compositing to explicitly build
        on the the simulation methods of the Virus object.
        """
        # virus object
        self.Virus = Virus
        # collected simulation data 
        self.t = []
        self.zeros = []
        self.A_count = []
        self.B_count = []
        self.C_count = []
        self.D_count = []
        self.R = []

    def vis_steps(self, FRAMES):
        """
        Saves a frame into the ./anim/ directory in addition
        to the simulation of the time step as defined in the Virus class.
        """
        # calculate changes in health and transmissions
        with alive_bar(FRAMES, bar="blocks") as bar:
            for F in range(FRAMES):
                self.Virus.time_step()
                # render frame
                self.frame(F, FRAMES)
                # move bar
                bar()

    def collect_data(self):
        """
        A: healthy
        B: sick / incubation 
        C: contagious
        D: immune
        """
        A = [[],[]]; B = [[],[]]; C = [[],[]]; D = [[],[]];

        wiggle = 0.7 # für leichte Bewegungen der Nodes für bessere allgemeine Sichtbarkeit
        for Nd in self.Virus.graph:
            x, y = Nd.coordinates[0] + random.random()*wiggle, Nd.coordinates[1] + random.random()*wiggle
            if Nd.infection_date == -1 and Nd.active:
                A[0].append(x); A[1].append(y)
            if Nd.infection_date != -1 and Nd.active:
                if V.time < Nd.infection_date + self.Virus.incubation_period:
                    B[0].append(x); B[1].append(y)
                else:
                    C[0].append(x); C[1].append(y)
            if Nd.active == False:
                D[0].append(x); D[1].append(y)

        return A, B, C, D

    def frame(self, F, FRAMES):
        """
        Creates a matplotlib figure displaying 
            + the positions and characteristics of all nodes representing people.
              (They can be 1.gray: healthy, 2.lgreen: sick, 3.dgreen: cantagious
              and 4.lblue: immune.)
            + the current distribution of node types as a bar chart
            + a history of the virus spread
        The figures are saved in the anim directory.
        """
        # sort all nodes into 4 categories for different scatter plots for ax2
        A, B, C, D = self.collect_data()

        # build the time data for ax1
        normal = len(A[0])
        infected = len(B[0])
        infectious = len(C[0])
        immune = len(D[0])
        self.B_count.append(len(B[0]))             # infected
        self.C_count.append(len(C[0])+len(B[0]))   # infectious + infected
        self.D_count.append(self.Virus.side_length**2 - len(D[0]))        # normal - (infectious + infected + immune)
        self.A_count.append(self.Virus.side_length**2)                  # max
        self.t.append(len(self.A_count))           # time
        self.zeros.append(0)                                    

        # plot style
        plt.style.use("default")
        plt.style.use("seaborn-dark")
        plt.style.use("grayscale")

        # create figure
        fig = plt.figure(figsize=(14,8), dpi=120)
        
        # timeline ratios
        ax1 = plt.Axes(fig=fig, rect=[0.024,0.42, 0.965, 0.55], facecolor='#f4f4f4')
        ax1.plot(self.t, self.A_count, "-")
        # fill between lines
        ax1.fill_between(self.t, self.B_count, self.zeros, color="#529959")
        ax1.fill_between(self.t, self.C_count, self.B_count, color="#2f630e")
        ax1.fill_between(self.t, self.D_count, self.C_count, color="#c4c4c4")
        ax1.fill_between(self.t, self.A_count, self.D_count, color="#7fadc6")
        ax1.set_ylim([0, self.Virus.side_length**2])
        ax1.set_yticks([])
        ax1.xaxis.set_major_locator(MultipleLocator(7))
        ax1.xaxis.set_minor_locator(MultipleLocator(1))
        ax1.tick_params(which='both', width=1.5)
        ax1.tick_params(which='major', length=7, color="gray", labelsize=16)
        ax1.tick_params(which='minor', length=4)
        ax1.set_xlim([1,FRAMES])
        ax1.set_xlabel("DAYS", size=20)
        # add axes to figure
        fig.add_axes(ax1)

        # plot of the simulation
        ax2 = plt.Axes(fig=fig, rect=[0., 1.0, 0.5, 0.88])
        # scatter plot of the nodes
        markersize = 35
        A_dots = ax2.scatter(A[0], A[1], c="#c4c4c4", s=markersize)
        D_dots = ax2.scatter(D[0], D[1], c="#7fadc6", s=markersize)
        B_dots = ax2.scatter(B[0], B[1], c="#529959", s=markersize)
        C_dots = ax2.scatter(C[0], C[1], c="#2f630e", s=markersize)
        # line plots of the containing box
        A_ = -0.5; B_ = self.Virus.side_length
        ax2.plot([A_,A_], [A_,B_], "-",  lw=3, color="gray")
        ax2.plot([A_,B_], [B_,B_], "-",  lw=3, color="gray")
        ax2.plot([B_,B_], [B_,A_], "-",  lw=3, color="gray")
        ax2.plot([B_,A_], [A_,A_], "-",  lw=3, color="gray")
        # don't display axes
        ax2.set_xticks([])
        ax2.set_yticks([])
        # Title
        ax2.text(0, 51.17 , "@QuentinWach | github.com/QuentinWach", size=13, fontweight='bold', color="silver")
        # add axes to figure
        fig.add_axes(ax2)

        # bar chart
        ax3 = plt.Axes(fig=fig, rect=[0.512, 1.042, 0.48, 0.48], facecolor="#f4f4f4")
        ax3.bar([0,1,2,3], [normal,infected,infectious,immune], color=["#c4c4c4", "#529959", "#2f630e", "#7fadc6"], 
            edgecolor="gray", linewidth=3, tick_label=["HEALTHY", "SICK", "INFECTIOUS", "IMMUNE"], width=0.8, bottom=None)
        ax3.tick_params(which='major', color="gray", labelsize=15)
        ax3.set_yticks([])
        ax3.set_ylim([0,self.Virus.side_length**2])
        ax3.text(-0.4, normal + 60, str(normal), size=40)
        ax3.text( 0.6, infected + 60, str(infected), size=40)
        ax3.text( 1.6, infectious + 60, str(infectious), size=40)
        ax3.text( 2.6, immune + 60, str(immune), size=40)
        # Wichtige Werte
        di = 210; he = (self.Virus.side_length ** 2) + 1140
        ax3.text(-0.5, he,      "Incubation Period:", size=20)
        ax3.text( 2.0, he,      "{} days".format(INC_PERIOD), size=20)
        ax3.text(-0.5, he-di*1, "Contagious Period:", size=20)
        ax3.text( 2.0, he-di*1, "{} days".format(CONT_PERIOD), size=20)
        ax3.text(-0.5, he-di*2, "Transmission Probability:", size=20)
        ax3.text( 2.0, he-di*2, "{} %".format(int(TRANSMISS*100)), size=20)
        ax3.text(-0.5, he-di*3, "Mobility Ratio:", size=20)   
        ax3.text( 2.0, he-di*3, "{} %".format(int(MOBILITY*100)), size=20)
        # Title
        ax3.text(-0.5, he+di*1.6,   "Virus Spread Toy Model", size=20, fontweight='bold')
        # add axes to figure
        fig.add_axes(ax3)
        
        # save
        plt.savefig("anim/" + str(self.Virus.time) + "_" + str(INC_PERIOD) + "_" + str(CONT_PERIOD) + "_" + str(TRANSMISS) + '.png', 
            bbox_inches="tight")
        plt.close()


# fixed parameters
random.seed(13931)
START_TIME = 0
FRAMES = 100
SIDE_LENGTH = 50        # TODO: enable different graph sizes for vis
INFECTED = 33
# testing paramenters
INC_PERIOD = 14         # min 1 to be plausible
CONT_PERIOD = 7
TRANSMISS = 0.2
MOBILITY = 0.5

# create a graph for the population
G = SquareGraph(SIDE_LENGTH, INFECTED, START_TIME)
# create the virus
V = Virus(START_TIME, INC_PERIOD, CONT_PERIOD, MOBILITY, TRANSMISS, G, SIDE_LENGTH)
# simulate the spread of the virus and render it 
VisualizeVirus(V).vis_steps(FRAMES)
# combine saved frames into a single mp4
movie.createVideo("anim", "videos/11.mp4")