# Quentin Wach
# AXES & TICKS CONTAINER IMAGE

import matplotlib.pyplot as plt
import matplotlib
import numpy as np
np.random.seed(42)

fig = plt.figure(figsize=(8,2), dpi=300)


ax1 = plt.Axes(fig=fig, rect=[0.51, 0.03, 0.48, 0.8], facecolor='white')
fig.add_axes(ax1)
ax1.set_xticks([]); ax1.set_yticks([])
ax1.tick_params(labelbottom=False, labelleft=False)
ax1.set_ylabel("Axis Container")
ax1.set_xlabel("Axis Container")
matplotlib.artist.getp(ax1)

N = 50
x1 = 0.0197 * np.arange(2,N)
y1 = 0.62 * np.random.rand(N-2) + 0.17 
ax1.plot(x1,y1,"o-", color="lightgray", alpha=0.85)
ax1.set_xlim([0,1])
ax1.set_ylim([0,1])

ax1.text(0.83,0.985,"Axes Container", color="black", size=10, horizontalalignment='center', backgroundcolor="white")
ax1.text(0,0.93," ", color="black", size=3, backgroundcolor="white", zorder=10)
ax1.text(0.963,0," ", color="black", size=3, backgroundcolor="white", zorder=10)

plt.arrow(0, 0, 0, 0.828, head_width=0.03, head_length=0.06, lw=3, fc='k', ec='k', zorder=30)
plt.arrow(0, 0, 0.9245, 0, head_width=0.07, head_length=0.025, lw=3, fc='k', ec='k', zorder=30)

plt.savefig("E7.svg", bbox_inches="tight")