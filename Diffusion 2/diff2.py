# Pixel Diffusion
"""
This time we will actually mix the particles.
The code will only save images of each iteration. You will
have to convert it to a gif or mp4 through different means.
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

res = 40
image_1 = np.ones((1*res,4*res))
image_2 = np.zeros((2*res,4*res))
image_3 = np.ones((1*res,4*res))
image = np.concatenate([image_1, image_2, image_3])

# for every timestep iterate through the pixel and diffuse
def diff(image):
    xmax, ymax = image.shape
    image_copy = image.copy()
    for x in range(xmax):
        for y in range(ymax):
            p = np.random.choice(8)
            # TODO: check if mixing up is even possible
            if p==1:
                try:
                    image_copy[x][y] = image[x-1][y-1]
                    image[x-1][y-1] = image[x][y]
                    image_copy[x-1][y-1] = image[x][y]
                except:
                    pass
            elif p==2:
                try:
                    image_copy[x][y] = image[x-1][y]
                    image[x-1][y] = image[x][y]
                    image_copy[x-1][y] = image[x][y]
                except:
                    pass
            elif p==3:
                try:
                    image_copy[x][y] = image[x-1][y+1]
                    image[x-1][y+1] = image[x][y]
                    image_copy[x-1][y+1] = image[x][y]
                except:
                    pass
            elif p==4:
                try:
                    image_copy[x][y] = image[x][y+1]
                    image[x][y+1] = image[x][y]
                    image_copy[x][y+1] = image[x][y]
                except:
                    pass
            elif p==5:
                try:
                    image_copy[x][y] = image[x+1][y+1]
                    image[x+1][y+1] = image[x][y]
                    image_copy[x+1][y+1] = image[x][y]
                except:
                    pass
            elif p==6:
                try:
                    image_copy[x][y] = image[x+1][y]
                    image[x+1][y] = image[x][y]
                    image_copy[x+1][y] = image[x][y]
                except:
                    pass
            elif p==7:
                try:
                    image_copy[x][y] = image[x+1][y-1]
                    image[x+1][y-1] = image[x][y]
                    image_copy[x+1][y-1] = image[x][y]
                except:
                    pass
            elif p==8:
                try:
                    image_copy[x][y] = image[x][y-1]
                    image[x][y-1] = image[x][y]
                    image_copy[x][y-1] = image[x][y]
                except:
                    pass
    return image_copy

plt.style.use("default")
plt.style.use("seaborn-dark")
plt.style.use("grayscale")
fig = plt.figure(figsize=(2, 2), dpi=200, facecolor='w', edgecolor='k', frameon=False)
ax = plt.Axes(fig, [0., 0., 1., 1.])
ax.set_axis_off()
ax.grid()
fig.add_axes(ax)
plt.xticks([])
plt.yticks([])

TIME = 400
ax.imshow(image, cmap="gray")
plt.savefig("img_" + str(0) + '.png')
for t in range(TIME):
    image = diff(image)
    ax.imshow(image)
    plt.savefig("img_" + str(t) + '.png')