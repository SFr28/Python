def ft_filter(function, iterable):
    "Filters the iterable item with the given funciton"

    newlist = [word for word in iterable if function(word)]
    return newlist
