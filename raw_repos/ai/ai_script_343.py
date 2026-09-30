def majorityElement(self, nums: List[int]):
    majority_count = len(nums)//2
    num_count = {}
    for num in nums:
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1
    for key, value in num_count.items():
        if value > majority_count:
            return key