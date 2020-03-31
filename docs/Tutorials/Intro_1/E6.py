import matplotlib.pyplot as plt
import matplotlib
import numpy as np

fig = plt.figure(figsize=(8,2), dpi=300)
f = plt.Axes(fig=fig, rect=[0,0,1,1], facecolor='lightgray')
fig.add_axes(f)     
ax1 = plt.Axes(fig=fig, rect=[0.51, 0.03, 0.48, 0.8], facecolor='white')
fig.add_axes(ax1)
ax2 = plt.Axes(fig=fig, rect=[0.01, 0.03, 0.48, 0.8], facecolor='white')
fig.add_axes(ax2)
ax1.set_xticks([]); ax1.set_yticks([])
ax2.set_xticks([]); ax2.set_yticks([])
f.set_xticks([]); f.set_yticks([])
ax1.text(0.5, 0.5, "Axes Container" , va="center", ha="center")
ax2.text(0.5, 0.5, "Axes Container" , va="center", ha="center")
ax1.tick_params(labelbottom=False, labelleft=False)
ax2.tick_params(labelbottom=False, labelleft=False)

N = 50
x1 = 0.021 * np.arange(N)
y1 = 0.42 * np.random.rand(N) 
x2 = 0.021* np.arange(N)
y2 = 0.42 * np.random.rand(N)
ax1.plot(x1,y1,"o-", color="lightgray", alpha=0.25)
ax2.plot(x2,y2,"o-", color="lightgray", alpha=0.25)
ax1.set_xlim([0,1])
ax1.set_ylim([0,1])
ax2.set_xlim([0,1])
ax2.set_ylim([0,1])




f.text(0.5,0.89,"Figure Container", color="black", size=10, horizontalalignment='center')


plt.savefig("E6.svg", bbox_inches="tight")