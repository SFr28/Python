import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from load_image import ft_load
from load_image import ft_zoom

def ft_rotate(img: np.ndarray) -> np.ndarray:
	'''Rotates the image'''

	rads = 90 * np.pi / 180.0
    
    # Let us find the height and width of the rotated image
	height_rot_img = round(abs(img.shape[0]*np.cos(rads))) + round(abs(img.shape[1]*np.sin(rads)))
	width_rot_img = round(abs(img.shape[1]*np.cos(rads))) + round(abs(img.shape[0]*np.sin(rads)))
	
	rot_img = np.uint8(np.zeros((height_rot_img,width_rot_img,img.shape[2])))
    
    # Finding the center point of the original image
	cx, cy = (img.shape[1]//2, img.shape[0]//2)

    # Finding the center point of rotated img.
	midx,midy = (width_rot_img//2, height_rot_img//2)
	
	for i in range(rot_img.shape[0]):
		for j in range(rot_img.shape[1]):
			x= (i-midx)*np.cos(rads)+(j-midy)*np.sin(rads)
			y= -(i-midx)*np.sin(rads)+(j-midy)*np.cos(rads)
			
			x=round(x)+cy
			y=round(y)+cx
			
			if (x>=0 and y>=0 and x<img.shape[0] and  y<img.shape[1]):
				rot_img[i,j,:] = img[x,y,:]
				
	return rot_img 

def main():

	img = ft_load("animal.jpeg")
	zoom = ft_zoom(img)
	print(zoom)

	rotated = ft_rotate(zoom)
	plt.imshow(rotated, cmap='gray')
	plt.show()


if __name__ == "__main__":
	main()