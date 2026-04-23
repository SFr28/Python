import numpy as np

def calculate_bmi(height, weight):
	'''Calculate the BMI with the given weight and height'''
	return weight / (height * height)

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:		
	'''Verify the height and weight lists given then calculate the BMI'''
	
	bmi = []
	bmi_ufunc = np.frompyfunc(calculate_bmi, 2, 1)

	try:
		if len(height) != len(weight):
			raise TypeError("Both lists must have the same size")
		
		height_arr = np.array(height)
		weight_arr = np.array(weight)

		if not np.issubdtype(height_arr.dtype, np.number):
			raise TypeError("Height must contain int or float")
		if not np.issubdtype(weight_arr.dtype, np.number):
			raise TypeError("Weight must contain int or float")
		
		bmi = bmi_ufunc(height_arr, weight_arr).tolist()

		
	except (ValueError, TypeError) as e:
		print(e)
	
	return bmi

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
	'''Check if the elements from the list are above the limit'''

	result = []

	for x in bmi:
		if x > limit:
			result.append(True)
		else:
			result.append(False)
	
	return result
