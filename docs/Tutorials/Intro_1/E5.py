import matplotlib.pyplot as plt
# for LaTeX font
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)


def annotate_axes(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
        ax.tick_params(labelbottom=False, labelleft=False)


fig = plt.figure(figsize=(8,8), dpi=200)
# color of figure border
fig.patch.set_facecolor('white')

ax1 = plt.Axes(fig=fig, rect=[0.3, 0.3, 0.4, 0.4], facecolor='crimson')
ax2 = plt.Axes(fig=fig, rect=[0, 0, 1, 1], facecolor='steelblue')
fig.add_axes(ax2)
fig.add_axes(ax1)

annotate_axes(fig)

# adjust spacing between subplots
plt.tight_layout()

ax1.grid()
ax2.grid()

# save graphic
plt.savefig("E5.svg", bbox_inches="tight")
plt.show()