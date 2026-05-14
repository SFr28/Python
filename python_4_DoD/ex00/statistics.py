def ft_statistics(*args: any, **kwargs: any) -> None:
    """
    Function that takes a serie of numbers and then calculate the \
    mean, median, quartile, standard deviation and variance \
    based on what the user asked (**in kwargs)
    """

    if len(args) != 0:
        try:
            serie = list(args)
            serie.sort()
            calculus = kwargs.values()
            for cal in calculus:
                match cal:
                    case "mean":
                        ft_mean(serie)
                    case "median":
                        ft_median(serie)
                    case "quartile":
                        ft_quartile(serie)
                    case "std":
                        ft_std_deviation(serie)
                    case "var":
                        ft_variance(serie)
        except (ValueError, TypeError, KeyError):
            print("Error")

    else:
        for i in kwargs:
            print("Error")


def ft_mean(serie: list) -> None:
    """function to caclulate mean"""
    mean = sum(serie) / len(serie)
    print(f"mean : {mean}")


def ft_median(nbs: list) -> None:
    """function to caclulate median"""
    if len(nbs) % 2 == 0:
        median = (nbs[int(len(nbs) / 2) - 1] + nbs[int(len(nbs))] / 2) / 2
    else:
        median = nbs[int(len(nbs) / 2)]
    print(f"median : {median}")


def ft_quartile(serie: list) -> None:
    """function to caclulate 1st and 3rd quartiles"""
    if len(serie) % 2 == 0 and (len(serie) / 2) % 2 == 0 or\
            len(serie) % 2 != 0 and (len(serie) / 2 - 1) % 2 == 0:
        posQ1 = int(len(serie) / 4)
        q1 = (serie[posQ1 - 1] + serie[posQ1]) / 2
        posQ3 = int(len(serie) / 2 + len(serie) / 4)
        q3 = (serie[posQ3 - 1] + serie[posQ3]) / 2
    else:
        q1 = float(serie[int(len(serie) / 4)])
        q3 = float(serie[int(len(serie) / 2 + len(serie) / 4)])
    quartile = [q1, q3]
    print(f"quartile : {quartile}")


def ft_std_deviation(serie: list) -> float:
    """function to caclulate standard deviation"""
    var = ft_variance(serie, False)
    std = var ** 0.5
    print(f"std : {std}")


def ft_variance(serie: list, display=True) -> None:
    """function to caclulate variance"""
    mean = sum(serie) / len(serie)
    diff = [(nb - mean) ** 2 for nb in serie]
    var = sum(diff) / len(serie)
    if display:
        print(f"var : {var}")
    return var
