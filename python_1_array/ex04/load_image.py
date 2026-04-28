import matplotlib.image as mpimg
import numpy as np


def ft_zoom(img: np.ndarray) -> np.ndarray:
    '''Zooms in on the image given'''
    zoom = img[100:500, 450:850, 0:1]
    zoom_in = zoom.reshape(400, 400)

    print("The shape of the image is:", zoom.shape, "or", zoom_in.shape)

    return zoom


def ft_load(path: str) -> np.ndarray:
    '''Loads an image with matplotlib and returns \
    an array with the RGB content'''
    img = mpimg.imread(path)
    array = np.asarray(img)

    return array
