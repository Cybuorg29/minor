def sort_dict(arr):
	arr.sort(key=lambda s: [s.lower(), s])
	return arr