import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    '''Slicing a 2D array based on start and end indexes'''

    try:
        if not isinstance(family, list):
            raise TypeError("The array must be a list")

        arr = np.array(family)
        if arr.ndim != 2:
            raise TypeError("The array must be a 2D list")
        print("My shape is : ", arr.shape)

        result = arr[start:end, :]
        print("My new shape is : ", result.shape)

        return result.tolist()

    except (ValueError, TypeError) as e:
        print(e)
        return []
