import matplotlib.pyplot as plt
# for LaTeX font
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)


def annotate_axes(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
        ax.tick_params(labelbottom=False, labelleft=False)


fig = plt.figure(figsize=(10,6), dpi=200)
# color of figure border
fig.patch.set_facecolor('white')
color = "silver"
ax1 = plt.subplot2grid((3, 5), (0, 0), colspan=5, facecolor=color)
ax2 = plt.subplot2grid((3, 5), (1, 0), colspan=2, facecolor=color)
ax3 = plt.subplot2grid((3, 5), (1, 2), rowspan=2, facecolor=color)
ax4 = plt.subplot2grid((3, 5), (2, 0), facecolor=color)
ax5 = plt.subplot2grid((3, 5), (2, 1), facecolor=color)
ax6 = plt.subplot2grid((3, 5), (1, 3), rowspan=2, colspan=2,facecolor=color)

annotate_axes(fig)

# save graphic
plt.savefig("E3.svg", bbox_inches="tight")
plt.show()