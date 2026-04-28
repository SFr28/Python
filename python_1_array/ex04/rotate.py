import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from load_image import ft_load
from load_image import ft_zoom

def ft_rotate(img: np.ndarray) -> np.ndarray:
	'''Rotates the image'''

	rotated = np.uint8(img).tolist()

	for i in range(img.shape[0]):
		for j in range(img.shape[1]):
			rotated[i][j] = img[j,i]

				
	return np.array(rotated)

def main():

	img = ft_load("animal.jpeg")
	zoom = ft_zoom(img)
	print(zoom)

	rotated = ft_rotate(zoom)
	plt.imshow(rotated, cmap='gray')
	plt.show()


if __name__ == "__main__":
	main()