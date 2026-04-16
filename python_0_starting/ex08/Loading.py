import os

def ft_tqdm(lst: range) -> None:

	total = len(lst)
	size = os.get_terminal_size()

	for i, elem in enumerate(lst):
		percent = (i + 1) / total
		filled = int((size[0] - 40) * percent)
		bar = '█' * filled + ' ' * (size[0] - 40 - filled)
		line = f'\r{int(percent * 100)}%|{bar}| {i + 1}/{total}'
		os.write(1, line.encode())
		yield elem
