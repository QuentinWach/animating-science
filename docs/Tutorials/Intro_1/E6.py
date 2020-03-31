import matplotlib.pyplot as plt
import matplotlib

def annotate_axes(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "Axes Container" , va="center", ha="center")
        ax.tick_params(labelbottom=False, labelleft=False)

fig = plt.figure(figsize=(8,2), dpi=300)


matplotlib.artist.getp(fig)
fig.set(frameon=False)
matplotlib.artist.getp(fig)

fig.text(0.5,1,"Figure Container", color="black", size=10, backgroundcolor="white", horizontalalignment='center')

annotate_axes(fig)

# adjust spacing between subplots
plt.tight_layout()

plt.savefig("E6.svg", bbox_inches="tight")