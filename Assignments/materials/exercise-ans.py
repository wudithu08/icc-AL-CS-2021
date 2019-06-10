import matplotlib.pyplot as plt
from copy import deepcopy

image = []


def zero(image, width, height):
    image.clear()
    for i in range(height):
        row = []
        for j in range(width):
            row.append(0)
        image.append(row)


# initialize a two dimensional array filled with zero
zero(image, 640, 640)


def upperLeftTriangle(image):
    # perform a deep copy, so we won't mess up with the image passed into this function
    image = deepcopy(image)
    # -------------- do whatever you want to "image" -----------
    height = len(image)
    width = len(image[0])
    for i in range(height):
        for j in range(0, width - i):
            image[i][j] = 255
    # ----------------------------------------------------------
    return image


def upperRightTriangle(image):
    # perform a deep copy, so we won't mess up with the image passed into this function
    image = deepcopy(image)
    # -------------- do whatever you want to "image" -----------
    height = len(image)
    width = len(image[0])
    for i in range(height):
        for j in range(i, width):
            image[i][j] = 255
    # ----------------------------------------------------------
    return image


def slices(image):
    # perform a deep copy, so we won't mess up with the image passed into this function
    image = deepcopy(image)
    # -------------- do whatever you want to "image" -----------
    height = len(image)
    width = len(image[0])
    for i in range(height):
        black = True
        for j in range(0, width, 100):
            for k in range(j, min(j + 100, width)):
                if black:
                    image[i][k] = 0
                else:
                    image[i][k] = 255
            black = not black
    # ----------------------------------------------------------
    return image


# create three subfigures
fig, (ax1, ax2, ax3) = plt.subplots(1, 3)

# plot images
ax1.imshow(upperLeftTriangle(image), cmap='gray', vmin=0, vmax=255)
ax2.imshow(upperRightTriangle(image), cmap='gray', vmin=0, vmax=255)
ax3.imshow(slices(image), cmap='gray', vmin=0, vmax=255)
plt.show()
