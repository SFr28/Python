import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np


def ft_load(path: str) -> np.ndarray:
    '''Loads an image with matplotlib and returns \
    an array with the RGB content'''

    img = mpimg.imread(path)
    array = np.asarray(img)

    print("The shape of the image is: ", array.shape)
    print(array)

    plt.subplot(3, 2, 1)
    plt.imshow(array)
    plt.axis('off')
    plt.title('Figure VIII.1: Original', y=-0.25)

    return array
