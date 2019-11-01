# Image Pixel Diffusion
"""
Building on Diffusion II we will now enhance this code
to be able to diffuse the pixels of any given image.
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.animation as animation
import math

image = np.asarray(mpimg.imread("Bild_1.png"))
print(image)
print(image.shape)

# for every timestep iterate through the pixel and diffuse
def diff(image):
    passed = 0
    xmax, ymax, zmax = image.shape
    image_copy = image.copy()
    for x in range(xmax):
        for y in range(ymax):
            p = np.random.choice(8) + 1
            # TODO: check if mixing up is even possible 
            if p==1:
                # check boundary condition (dont diffuse opposing sides)
                if (x != 0) and (y != 0): 
                    """                    
                    # check if diff is even possible
                    if image[x][y] == image[x-1][y-1]:
                        print("diff not possible!")
                        passed += 1
                    """
                    try:
                        image_copy[x][y] = image[x-1][y-1]
                        image[x-1][y-1] = image[x][y]
                        image_copy[x-1][y-1] = image[x][y]
                    except:
                        pass
                else:
                    passed += 1
                    pass
            elif p==2:
                if (x != 0):
                    try:
                        image_copy[x][y] = image[x-1][y]
                        image[x-1][y] = image[x][y]
                        image_copy[x-1][y] = image[x][y]
                    except:
                        pass
                else:
                    passed += 1
                    pass
            elif p==3:
                if (x != 0) and (y != ymax-1):
                    try:
                        image_copy[x][y] = image[x-1][y+1]
                        image[x-1][y+1] = image[x][y]
                        image_copy[x-1][y+1] = image[x][y]
                    except:
                        pass
                else:
                    passed += 1
                    pass
            elif p==4:
                if (y != ymax-1):
                    try:
                        image_copy[x][y] = image[x][y+1]
                        image[x][y+1] = image[x][y]
                        image_copy[x][y+1] = image[x][y]
                    except:
                        pass
                else:
                    passed += 1
                    pass
            elif p==5:
                if (x != xmax-1) and (y != ymax-1):
                    try:
                        image_copy[x][y] = image[x+1][y+1]
                        image[x+1][y+1] = image[x][y]
                        image_copy[x+1][y+1] = image[x][y]
                    except:
                        pass
                else:
                    passed += 1
                    pass
            elif p==6:
                if (x != xmax-1):
                    try:
                        image_copy[x][y] = image[x+1][y]
                        image[x+1][y] = image[x][y]
                        image_copy[x+1][y] = image[x][y]
                    except:
                        pass
                else:
                    passed += 1
                    pass
            elif p==7:
                if (x != xmax-1) and (y != 0):
                    try:
                        image_copy[x][y] = image[x+1][y-1]
                        image[x+1][y-1] = image[x][y]
                        image_copy[x+1][y-1] = image[x][y]
                    except:
                        pass
                else:
                    passed += 1
                    pass
            elif p==8:
                if (y != 0):                
                    try:
                        image_copy[x][y] = image[x][y-1]
                        image[x][y-1] = image[x][y]
                        image_copy[x][y-1] = image[x][y]
                    except:
                        pass
                else:
                    passed += 1
                    pass

    print("Passed: " + str(passed))
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

TIME = 60
DIFFS = 1
for t in range(TIME):
    ax.imshow(image)
    plt.savefig("img_" + str(t) + '.png')
    DIFFS += 1
    if DIFFS <= 12:
        DIFFS = int(abs(math.sqrt(DIFFS ** 3)))
    for _ in range(DIFFS):
        image = diff(image)
    print(t)
    ax.imshow(image)
    plt.savefig("img_" + str(t+1) + '.png')
