def median(my_list):
	half = len(my_list)//2
	my_list.sort()
	median_index = len(my_list) - half
	return my_list[median_index]

The suggested modification is to add a sorting step to the code before finding the median index. This will ensure the list is always in order and the median index can be found in an efficient manner.