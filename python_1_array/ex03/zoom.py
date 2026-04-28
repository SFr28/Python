import matplotlib.pyplot as plt
import numpy as np
from load_image import ft_load


def ft_zoom(img: np.ndarray) -> np.ndarray:
    '''Zooms in on the image given'''
    zoom = img[100:500, 450:850, 0:1]
    zoom_in = zoom.reshape(400, 400)

    print("\nNew shape after slicing:", zoom.shape, "or", zoom_in.shape)

    return zoom


def main():
    img = ft_load("animal.jpeg")
    print(img)

    zoom = ft_zoom(img)
    print(zoom)
    plt.imshow(zoom, cmap='gray')
    plt.show()


if __name__ == "__main__":
    main()
