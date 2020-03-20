import matplotlib.pyplot as plt

# for LaTeX font
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)

# extension for scientific computing
import numpy as np

# x tics
X = np.arange(-2,4,0.003)

# line
Y = []
for x in X:
    y = ((x-1)**3 + 1)
    Y.append(y)

# random dots around line
Y2 = []
for x in X:
    y2 = ((x-1)**3 + 1) + (np.random.normal(0,2))
    Y2.append(y2)

# create the figure
fig, ax = plt.subplots(1,figsize=(5,3), dpi=200)

# color of figure border
fig.patch.set_facecolor('white')

# data plotting
ax.plot(X,Y2,".", markersize=1)
ax.plot(X,Y,"-", color="crimson")

# y-axis
plt.ylabel(r"$y$")
plt.ylim(-20, 20)
# x-axis
plt.xlabel(r"$x$")
plt.xlim(-2, 4) 

# LaTeX function
plt.text(0.45,8.5,r"$(x-1)^3 + 1$", color="crimson", size=10)

# save graphic
plt.savefig("E1.svg", bbox_inches="tight")

# show graphic
plt.show()
