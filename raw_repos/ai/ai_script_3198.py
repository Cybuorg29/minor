def flatten_dict(d):
	flattened_dict = {}

	for key, val in d.items():
		if type(val) is dict: # if val is a dict
			for k, v in val.items():
				flattened_dict[key + "_" + k] = v
		else:
			flattened_dict[key] = val

	return flattened_dict

if __name__ == '__main__':
	d = {"a": 1, "b": {"c": 2, "d": 3}}
	print(flatten_dict(d))