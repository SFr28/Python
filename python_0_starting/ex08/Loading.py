import os

def ft_tqdm(lst: range) -> None:
	"Shows a loading bar based on the range given"

	total = len(lst)
	size = os.get_terminal_size()

	for i, elem in enumerate(lst):
		if i % 10 == 9 and i < total - 10:
			percent = (i + 1) / total
			filled = int((size[0] - 40) * percent)
			bar = '█' * filled + ' ' * (size[0] - 40 - filled)
			line = f'\r{int(percent * 100)}%|{bar}| {i + 1}/{total}'
			os.write(1, line.encode())
		elif i >= total - 10:
			percent = (i + 1) / total
			filled = int((size[0] - 40) * percent)
			bar = '█' * filled + ' ' * (size[0] - 40 - filled)
			line = f'\r{int(percent * 100)}%|{bar}| {i + 1}/{total}'
			os.write(1, line.encode())
		yield elem
