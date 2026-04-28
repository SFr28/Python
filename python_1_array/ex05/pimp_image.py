import matplotlib.pyplot as plt
import numpy as np
from load_image import ft_load

def ft_invert(array) -> np.ndarray:
	'''Inverts the colors of the image received'''

	print("invert")

	if array.ndim != 3 or array.shape[2] != 3:
		raise TypeError("Image must be represented by a 3D array with 3 color codes")

	inverted = np.uint8(255 - array)

	plt.subplot(3, 2, 2)
	plt.imshow(inverted)
	plt.axis('off')
	plt.title('Figure VIII.2: Invert', y=-0.25)

	return inverted


def ft_red(array) -> np.ndarray:
	'''Colors the image received in red by only keeping the red component (RGB => 1st component)'''

	print("red")
	
	if array.ndim != 3 or array.shape[2] != 3:
		raise TypeError("Image must be represented by a 3D array with 3 color codes")
	
	reded = np.zeros_like(array)
	reded[:,:,0] = array[:,:,0]

	plt.subplot(3, 2, 3)
	plt.imshow(reded)
	plt.axis('off')
	plt.title('Figure VIII.3: Red', y=-0.25)

	return (reded)

def ft_green(array) -> np.ndarray:
	'''Colors the image received in green by only keeping the green component (RGB => 2nd component)'''

	print("green")
	
	if array.ndim != 3 or array.shape[2] != 3:
		raise TypeError("Image must be represented by a 3D array with 3 color codes")
	

	greened = np.zeros_like(array)
	greened[:,:,1] = array[:,:,1]

	plt.subplot(3, 2, 4)
	plt.imshow(greened)
	plt.axis('off')
	plt.title('Figure VIII.4: Green', y=-0.25)

	return (greened)

def ft_blue(array) -> np.ndarray:
	'''Colors the image received in blue by only keeping the blue component (RGB => 3rd component)'''

	print("blue")
	
	if array.ndim != 3 or array.shape[2] != 3:
		raise TypeError("Image must be represented by a 3D array with 3 color codes")
	
	blued = np.zeros_like(array)
	blued[:,:,2] = array[:,:,2]

	plt.subplot(3, 2, 5)
	plt.imshow(blued)
	plt.axis('off')
	plt.title('Figure VIII.5: Blue', y=-0.25)

	return (blued)

def ft_grey(array) -> np.ndarray:
	'''Colors the image received in grey by calculating the mean value'''

	print("grey")
	
	if array.ndim != 3 or array.shape[2] != 3:
		raise TypeError("Image must be represented by a 3D array with 3 color codes")

	greyed = np.mean(array, axis=2).astype(np.uint8)

	plt.subplot(3, 2, 6)
	plt.imshow(greyed, cmap='gray')
	plt.axis('off')
	plt.title('Figure VIII.6: Grey', y=-0.25)

	return (greyed)


def main():

	try:
		array = ft_load("landscape.jpg")

		ft_invert(array)
		ft_red(array)
		ft_green(array)
		ft_blue(array)
		ft_grey(array)

		plt.show()
	
	except (ValueError, TypeError) as e:
		print(e)


if __name__ == "__main__":
	main()