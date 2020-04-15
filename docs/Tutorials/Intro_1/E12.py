import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# create figure
fig = plt.figure(figsize=(2.5,2.5),dpi=200)

# create axes object
ax = plt.Axes(fig=fig, rect=[0, 0, 1, 1], facecolor='crimson')
fig.add_axes(ax)

# change x-axis major tick lcoations
ax.xaxis.set_major_locator(ticker.FixedLocator([0,0.4,0.7, 1]))

plt.savefig("E12.svg", bbox_inches="tight")