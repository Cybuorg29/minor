def kthSmallest(arr, k): 
	# Sort the given array 
	arr.sort() 

	# Return k'th element in  
	# the sorted array 
	return arr[k-1]