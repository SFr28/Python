def ft_filter(function, iterable):
    """
    Return an iterator yielding those items of iterable for which
    function(item) is true.
    If function is None, return the items that are true.
    """

    if function is None:
        newlist = [word for word in iterable if word]
    else:
        newlist = [word for word in iterable if function(word)]
    return newlist
