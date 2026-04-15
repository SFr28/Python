def ft_filter(function, iterable):
	newlist = [word for word in iterable if function(word)]
	return newlist