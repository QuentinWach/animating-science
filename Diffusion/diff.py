# Diffusion
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
plt.style.use("default")
plt.style.use("seaborn-dark")
plt.style.use("grayscale")
fig, ax = plt.subplots(figsize=(8,8),dpi=120)
fig.patch.set_facecolor('white')
fig.canvas.set_window_title('Diffusion')

# draw circles with a lot of dots
dots = 3000
frames = 300
change_int = 0.005

# init dot positions
dot_pos_x = []
dot_pos_y = []
for d in range(dots):
    for r in range(5):
        x = 0.1 * (r+1) * np.cos(2*np.pi * d / dots)
        y = 0.1 * (r+1) * np.sin(2*np.pi * d / dots)
        dot_pos_x.append(x)
        dot_pos_y.append(y)

# diffuse the dots over time
plot, = ax.plot(dot_pos_x, dot_pos_y, ".", markersize=0.75)
def diff(i):
    for d in range(len(dot_pos_x)):
        dot_pos_x[d] = dot_pos_x[d] + (np.random.rand(1)*2-1) * change_int
    for d in range(len(dot_pos_y)):
        dot_pos_y[d] = dot_pos_y[d] + (np.random.rand(1)*2-1) * change_int
    print(i)
    plot.set_data(dot_pos_x, dot_pos_y)

# show (and save) the animation
anim = animation.FuncAnimation(fig, diff, frames=frames, interval=1)
#anim.save('diff_anim2.mp4', writer='ffmpeg', fps=60, bitrate=1600)
plt.show()
