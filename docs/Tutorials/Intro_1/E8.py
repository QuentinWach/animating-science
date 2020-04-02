import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10,6), dpi=(200))

ax1 = fig.add_subplot(421, facecolor="silver") # ax1
ax2 = fig.add_subplot(423, facecolor="silver") # ax2
ax3 = fig.add_subplot(223, facecolor="silver") # ax3

ax4 = fig.add_axes([0.77,.3,.2,.6], facecolor="silver") # ax4
ax5 = fig.add_axes([0.61,.5,.2,.3], facecolor="silver") # ax5
ax6 = fig.add_axes([0.6,.1,.35,.3], facecolor="silver") # ax6

ax1.set_xticks([]); ax1.set_yticks([])
ax2.set_xticks([]); ax2.set_yticks([])
ax3.set_xticks([]); ax3.set_yticks([])
ax3.text(0.320,-0.1,"Axes on a grid (Subplots)")
ax4.set_xticks([]); ax4.set_yticks([])
ax5.set_xticks([]); ax5.set_yticks([])
ax6.set_xticks([]); ax6.set_yticks([])
ax6.text(0.32,-0.245,"directly added Axes")

ax1.tick_params(labelbottom=False, labelleft=False)
ax2.tick_params(labelbottom=False, labelleft=False)

def annotate_axes(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
        ax.tick_params(labelbottom=False, labelleft=False)

annotate_axes(fig)

plt.tight_layout()
plt.savefig("E8.svg", bbox_inches="tight")
#plt.show()