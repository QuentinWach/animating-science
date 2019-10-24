# Image Pixel Diffusion
"""
Building on Diffusion II we will now enhance this code
to be able to diffuse the pixels of any given image.
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.animation as animation

image = np.asarray(mpimg.imread("Bild_1.jpg"))
print(image)
print(image.shape)

# for every timestep iterate through the pixel and diffuse
def diff(image):
    xmax, ymax, zmax = image.shape
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
ax.imshow(image)
plt.savefig("img_" + str(0) + '.png')
for t in range(TIME):
    image = diff(image)
    ax.imshow(image)
    plt.savefig("img_" + str(t) + '.png')