import matplotlib.pyplot as plt

# for LaTeX font
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)

# linear algebra extension
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

# create the figure and subplots
fig, axs = plt.subplots(1,2,figsize=(8,3), dpi=200)
# color of figure border
fig.patch.set_facecolor('white')

# SUBPLOT 1
axs[0].set_title(r"Dummy data $f(x)$", size=10)
# data plotting
axs[0].plot(X,Y2,".", markersize=1, color="steelblue")
axs[0].plot(X,Y,"-", color="crimson")
# y-axis
axs[0].set_ylabel(r"$y$",labelpad=-5)
axs[0].set_ylim(-20, 20)
# x-axis
axs[0].set_xlabel(r"$x$")
axs[0].set_xlim(-2, 4)
# LaTeX function
axs[0].text(0.15,-12.5,r"$f(x) = \big[ (x-1)^3 + 1 \big] + n(x)$", color="steelblue", size=10) # color="crimson"

# SUBPLOT 2
axs[1].set_title(r"Normal distribution $n(x)$", size=10)
# data plotting
mu, sigma = 0, 2 # mean and standard deviation
s = np.random.normal(mu, sigma, int(6//0.003))
count, bins, ignored = axs[1].hist(s, 300, density=True, color="steelblue")
axs[1].plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) 
    * np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
    color="black")
# x-axis
axs[1].set_xlabel(r"$x$")
axs[1].set_xlim(-4.5, 4.5)
# y-axis
axs[1].yaxis.set_label_position("right")
axs[1].yaxis.tick_right()
axs[1].set_ylabel(r"Probability density",labelpad=5)
axs[1].set_ylim(0, 0.25)
axs[1].text(-4.,0.21,r"$\mu = 0$", color="black", size=10)
axs[1].text(-4.,0.192,r"$\sigma = 2$", color="black", size=10)


# adjust spacing between subplots
plt.tight_layout()

# save graphic
plt.savefig("E2.svg", bbox_inches="tight")

# show graphic
plt.show()
