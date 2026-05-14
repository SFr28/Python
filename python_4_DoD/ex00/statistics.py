def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    Function that takes a serie of numbers and then calculate the \
    mean, median, quartile, standard deviation and variance \
    based on what the user asked (**in kwargs)
    """

    if len(args) == 0:
        for i in kwargs:
            print('ERROR')
        return

    match kwargs:
        case "mean":
        case "median":
        case "quartile":
        case "std":
        case "var":
