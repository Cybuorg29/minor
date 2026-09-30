def calculateAverage(nums):
    average = 0
    for num in nums:
        average += num
    return average / len(nums)

print(calculateAverage([1,7,8,10]))
# Output: 6.5