"""
Create a program to generate the sum of all the elements in a given list
"""

def sum_list(nums):
    total = 0
    for num in nums:
        total += num
    return total

if __name__ == '__main__':
    print(sum_list([1, 2, 3, 4, 5]))