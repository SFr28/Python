def square(x: int | float) -> int | float:
    """Function that returns the square of the argument"""
    try:
        if not isinstance(x, (int, float)):
            raise TypeError("x must be an int or a float")

        return x ** 2

    except TypeError as e:
        print("TypeError:", e)
    except OverflowError as e:
        print("OverflowError: ", e)
    except Exception as e:
        print(f"An unexpected error occurred in square(): {e}")


def pow(x: int | float) -> int | float:
    """Function that returns the exponention of arg by itself"""
    try:
        if not isinstance(x, (int, float)):
            raise TypeError("x must be an int or a float")

        return x ** x

    except TypeError as e:
        print("TypeError:", e)
    except OverflowError as e:
        print("OverflowError: ", e)
    except Exception as e:
        print(f"An unexpected error occurred in pow(): {e}")


def outer(x: int | float, function) -> object:
    """
    Outer function that returns an object which, when called,
    returns the result of the arguments calculation
    """

    try:
        if not callable(function):
            raise TypeError("Second argument must be a function")

        count = 0

        def inner() -> float:
            """
            Inner function that takes the outer's function
            and uses it with the outer's nb
            Updates the count and returns the function's result
            """
            nonlocal count
            nb = function(x)
            for c in range(count):
                nb = function(nb)
            count += 1
            return nb
        return inner

    except TypeError as e:
        print("TypeError:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)
    return str
