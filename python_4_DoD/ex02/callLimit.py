def callLimit(limit: int):
    """
    Takes a limit to apply to a function
    """
    count = 0

    def callLimiter(function):
        """
        Count the number of times the function has been called
        """
        def limit_function(*args: any, **kwds: any):
            """
            Checks if the limit has been reached or not
            """
            nonlocal count
            count += 1
            if (limit >= count):
                return function(*args, **kwds)
            else:
                print(f"Error: {function} call too many times")
        return limit_function
    return callLimiter
