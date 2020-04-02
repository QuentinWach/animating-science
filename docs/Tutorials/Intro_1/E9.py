import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

fig = plt.figure(figsize=(8,5), dpi=200)

# background grid
b = plt.Axes(fig=fig, rect=[0, 0, 1, 1], facecolor="white")
b.grid(b=True, color='gray', linestyle="--", linewidth=1)
# change ticks
b.xaxis.set_major_locator(ticker.MultipleLocator(1/8))
b.yaxis.set_major_locator(ticker.MultipleLocator(1/5))
b.tick_params(bottom=False, left=False, labelbottom=False, labelleft=False)
# add axes
fig.add_axes(b)
# delete border box without deleting the gridlines
plt.box(False)

# subplots
ax1 = fig.add_axes([0.006,0.01 + 4/5,1/2 - 0.012,1/5 - 0.02], facecolor="silver") # ax2
ax2 = fig.add_axes([0.006,0.01 + 3/5,1/2 - 0.012,1/5 - 0.02], facecolor="silver") # ax1
ax3 = fig.add_axes([0.006,0.01,1/2 - 0.012,3/5 - 0.02], facecolor="silver") # ax3
ax1.set_xticks([]); ax1.set_yticks([])
ax2.set_xticks([]); ax2.set_yticks([])
ax3.set_xticks([]); ax3.set_yticks([])
ax1.tick_params(labelbottom=False, labelleft=False)
ax2.tick_params(labelbottom=False, labelleft=False)
ax3.tick_params(labelbottom=False, labelleft=False)

# axes
ax4 = fig.add_axes([0.77,.3,.2,.6], facecolor="silver") # ax4
ax5 = fig.add_axes([0.61,.52,.2,.3], facecolor="silver") # ax5
ax6 = fig.add_axes([0.57,.14,.35,.3], facecolor="silver") # ax6
ax4.set_xticks([]); ax4.set_yticks([])
ax5.set_xticks([]); ax5.set_yticks([])
ax6.set_xticks([]); ax6.set_yticks([])
ax4.tick_params(labelbottom=False, labelleft=False)
ax5.tick_params(labelbottom=False, labelleft=False)
ax6.tick_params(labelbottom=False, labelleft=False)

# add text
ax3.text(0.278,-0.1,"Axes on a grid (Subplots)", backgroundcolor="white")
ax6.text(0.25,-0.245,"directly added Axes", backgroundcolor="white")

# print the names of the axes
def annotate_axes(fig):
    for i, ax in enumerate(fig.axes):
        if i != 0:
            ax.text(0.5, 0.5, "ax%d" % (i), va="center", ha="center")
            ax.tick_params(labelbottom=False, labelleft=False)
annotate_axes(fig)

# save graphic
plt.savefig("E9.svg", bbox_inches="tight")
#plot.show()