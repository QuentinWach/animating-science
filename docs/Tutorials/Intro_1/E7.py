# Quentin Wach
# AXES & TICKS CONTAINER IMAGE

import matplotlib.pyplot as plt
import matplotlib
import numpy as np

fig = plt.figure(figsize=(16,4), dpi=300)


ax1 = plt.Axes(fig=fig, rect=[0.51, 0.03, 0.48, 0.8], facecolor='white')
fig.add_axes(ax1)
ax1.set_xticks([]); ax1.set_yticks([])
ax1.tick_params(labelbottom=False, labelleft=False)
ax1.set_ylabel("Axis Container")
ax1.set_xlabel("Axis Container")
matplotlib.artist.getp(ax1)

N = 50
x1 = 0.021 * np.arange(0.3,N)
y1 = 0.62 * np.random.rand(N) + 0.17 
ax1.plot(x1,y1,"o-", color="lightgray", alpha=0.85)
ax1.set_xlim([0,1])
ax1.set_ylim([0,1])

ax1.annotate("", xy=(0.99, 0.0), xytext=(0, 0),arrowprops=dict(arrowstyle="->"))
ax1.annotate("", xy=(0.0, 0.975), xytext=(0, 0), arrowprops=dict(arrowstyle="->"), backgroundcolor="white")

ax1.text(0.83,0.985,"Axes Container", color="black", size=10, horizontalalignment='center', backgroundcolor="white")

plt.savefig("E7.svg", bbox_inches="tight")