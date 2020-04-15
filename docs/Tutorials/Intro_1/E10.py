import  matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from itertools import product


# FIGURE SETUP
fig = plt.figure(figsize=(4, 4), dpi=200, constrained_layout=False)


# A 
b = plt.Axes(fig=fig, rect=[0, 0, 1, 1], facecolor="white")
b.grid(b=True, color='black', linestyle="--", linewidth=1)
# change ticks
b.xaxis.set_major_locator(ticker.MultipleLocator(1/2))
b.yaxis.set_major_locator(ticker.MultipleLocator(1/2))
b.tick_params(bottom=False, left=False, labelbottom=False, labelleft=False)
# add axes
fig.add_axes(b)
# delete border box without deleting the gridlines
plt.box(False)

# B 
b = plt.Axes(fig=fig, rect=[1.02, 0.05, 0.3, 0.63], facecolor="white")
b.grid(b=True, color='black', linestyle="--", linewidth=1)
# change ticks
b.xaxis.set_major_locator(ticker.MultipleLocator(1/3))
b.yaxis.set_major_locator(ticker.MultipleLocator(1/6))
b.tick_params(bottom=False, left=False, labelbottom=False, labelleft=False)
# add axes
fig.add_axes(b)
# delete border box without deleting the gridlines
plt.box(False)

# C
b = plt.Axes(fig=fig, rect=[1.119, 0.7, 0.3, 0.3], facecolor="white")
b.grid(b=True, color='black', linestyle="--", linewidth=1)
# change ticks
b.xaxis.set_major_locator(ticker.MultipleLocator(1/4))
b.yaxis.set_major_locator(ticker.MultipleLocator(1/4))
b.tick_params(bottom=False, left=False, labelbottom=False, labelleft=False)
# add axes
fig.add_axes(b)
# delete border box without deleting the gridlines
plt.box(False)

# D
b = plt.Axes(fig=fig, rect=[1.4, 0.198, 0.5, 0.38], facecolor="white")
b.grid(b=True, color='black', linestyle="--", linewidth=1)
# change ticks
b.xaxis.set_major_locator(ticker.MultipleLocator(1/2))
b.yaxis.set_major_locator(ticker.MultipleLocator(1/2))
b.tick_params(bottom=False, left=False, labelbottom=False, labelleft=False)
# add axes
fig.add_axes(b)
# delete border box without deleting the gridlines
plt.box(False)

# E
b = plt.Axes(fig=fig, rect=[0.51, 0.51, 0.48, 0.48], facecolor="white")
b.grid(b=True, color='black', linestyle="--", linewidth=1)
# change ticks
b.xaxis.set_major_locator(ticker.MultipleLocator(1/2))
b.yaxis.set_major_locator(ticker.MultipleLocator(1/2))
b.tick_params(bottom=False, left=False, labelbottom=False, labelleft=False)
# add axes
fig.add_axes(b)
# delete border box without deleting the gridlines
plt.box(False)

# F
b = plt.Axes(fig=fig, rect=[0.52, 0.52, 0.22, 0.22], facecolor="white")
b.grid(b=True, color='black', linestyle="--", linewidth=1)
# change ticks
b.xaxis.set_major_locator(ticker.MultipleLocator(1/4))
b.yaxis.set_major_locator(ticker.MultipleLocator(1/4))
b.tick_params(bottom=False, left=False, labelbottom=False, labelleft=False)
# add axes
fig.add_axes(b)
# delete border box without deleting the gridlines
plt.box(False)


plt.savefig("E10.svg", bbox_inches="tight")