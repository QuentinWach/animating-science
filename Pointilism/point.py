# Image Point Cloud
"""
CHAOTIC MINIMALISM
1) Creates a minimalist b&w point cloud of a given image.
TODO:
2) Draw 3 closed lines (RGB) with varying distance to give the image color (chaotic crossing? YES) 
3) Give lines more texture/variaton fulidity
3) experiment with randomness
4) produce/print the artworks
"""
#====================
res = 10
mk = 5
#====================

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.animation as animation

# load image (prepare for turning it bw) 
image = np.asarray(mpimg.imread("Vorlage.jpg"))
image = image[:, :, 0]


# cut image so that it can be scaled down by the resolution res
while image.shape[0]%res!=0:
    image = image[:image.shape[0]-1,:]
while image.shape[1]%res!=0:
    image = image[:,:image.shape[1]-1]

# subdivide image into pixels with given resolution
xmax, ymax = image.shape
new_shape = (int(xmax/res), int(ymax/res))
new_image = np.zeros(new_shape)
print("Image Shape Orig: " + str(image.shape))
print("Image Shape Now: " + str(new_shape))

v_sum = 0
for x in range(xmax):
    for y in range(ymax):
        # mean image values
        v_sum += image[x,y]
        # create new image
        if y%res==0:
            v_mean = v_sum/res
            v_sum = 0
            x_pos = int((x/res))
            y_pos = int((y/res)-1)
            # create scaled image
            new_image[x_pos,y_pos] = v_mean




# show the artwork
plt.style.use("default")
plt.style.use("seaborn-dark")
plt.style.use("grayscale")
fig = plt.figure(figsize=(new_shape[1]/10,new_shape[0]/10), dpi=300, facecolor='w', edgecolor='k', frameon=False) #dpi=300
ax = plt.Axes(fig, [0., 0., 1., 1.])
ax.set_axis_off()
ax.grid()
fig.add_axes(ax)
plt.xticks([])
plt.yticks([])
def points():
    # generating dot data
    dot_image_x = []
    dot_image_y = []
    dot_value = []
    for x in range(new_image.shape[1]):
        for y in range(new_image.shape[0]):
            dot_image_x.append(x)
            dot_image_y.append(y)
            try:
                # ACHTUNG!!!: Bei .png die /255 löschen!!!
                dot_value.append(mk* np.log(1/(new_image[y,x]/255))**0.5)
            except:
                pass

    print(dot_value)

    # plot the dots
    for dot in range(len(dot_image_x)):
        print("...plotting " + str(dot) + " / " + str(new_shape[0]*new_shape[1]))
        try:
            plt.plot(dot_image_x[dot], -dot_image_y[dot], "o", markersize=dot_value[dot], color="black")
        except:
            pass

points()
#plt.imshow(new_image, cmap="gray")

print("yeah!")
plt.savefig("Ergebnis_3_1.png")
