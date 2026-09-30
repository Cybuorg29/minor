# Finds two numbers in an array that have the largest sum
def getMaxSum(arr):
    # Initialize the sum to the maximum possible value
	maxSum = -float('inf')
	
	# Iterate over all elements of the array
	for i in range(len(arr)):
		for j in range(i+1, len(arr)):
			# Compare the current sum to the maximum sum
			maxSum = max(maxSum, arr[i] + arr[j])

    # Return the largest sum
	return maxSum