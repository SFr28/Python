import matplotlib.image as mpimg
import numpy as np

def ft_load(path: str) -> np.ndarray:
	'''Load an image with matplotlib and returns an array with the RGB content'''
	img = mpimg.imread(path)
	array = np.asarray(img)

	print("The shape of the image is: ", array.shape)

	return array