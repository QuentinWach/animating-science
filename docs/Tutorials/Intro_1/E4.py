import matplotlib.pyplot as plt
# for LaTeX font
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)


def annotate_axes(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
        ax.tick_params(labelbottom=False, labelleft=False)


fig = plt.figure(figsize=(8,4), dpi=200)
# color of figure border
fig.patch.set_facecolor('white')
color = "silver"
ax1 = plt.subplot2grid((2, 2), (0, 0), facecolor=color)
ax2 = plt.subplot2grid((2, 2), (1, 0), facecolor=color)
ax3 = plt.subplot2grid((2, 2), (0, 1), facecolor=color)
ax4 = plt.subplot2grid((2, 2), (1, 1), facecolor=color)

annotate_axes(fig)

# adjust spacing between subplots
plt.tight_layout()

# save graphic
plt.savefig("E4.svg", bbox_inches="tight")
plt.show()