#!/bin/python
import numpy as np


def calculate_bmi(height, weight):
    '''Calculate the BMI with the given weight and height'''
    return weight / (height * height)


def give_bmi(h: list[int | float], w: list[int | float]) -> list[int | float]:
    '''Verify the height and weight lists given then calculate the BMI'''

    bmi = []
    bmi_ufunc = np.frompyfunc(calculate_bmi, 2, 1)

    try:
        if len(h) != len(w):
            raise TypeError("Both lists must have the same size")

        h_arr = np.array(h)
        w_arr = np.array(w)

        if not np.issubdtype(h_arr.dtype, np.number):
            raise TypeError("Height must contain int or float")
        if not np.issubdtype(w_arr.dtype, np.number):
            raise TypeError("Weight must contain int or float")

        bmi = bmi_ufunc(h_arr, w_arr).tolist()

    except (ValueError, TypeError) as e:
        print(e)

    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    '''Check if the elements from the list are above the limit'''

    result = []

    try:
        if not isinstance(bmi, list):
            raise TypeError("bmi must be a list")
        for x in bmi:
            if x > limit:
                result.append(True)
            else:
                result.append(False)

    except TypeError as e:
        print(e)

    return result
