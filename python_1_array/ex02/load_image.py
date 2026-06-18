import matplotlib.image as mpimg
import numpy as np


def ft_load(path: str) -> np.ndarray:
    '''Loads an image with matplotlib and returns \
    an array with the RGB content'''
    try:
        if path.find(".jpg") != len(path) - 4 and\
                path.find(".jpeg") != len(path) - 5:
            raise TypeError("not a jpg or jpeg")
        img = mpimg.imread(path)
        array = np.asarray(img)

        print("The shape of the image is: ", array.shape)
        return array

    except TypeError as e:
        print("Type error:", e)
    except Exception as e:
        print("Error:", e)
