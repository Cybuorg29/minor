"""
Count the number of occurrences of a given number in a list of numbers.
"""

numbers = [1,1,2,3,4,4,4,5]
number = 4

def count_occurrences(numbers, number):
    count = 0
    for num in numbers:
        if num == number:
            count += 1
    return count

print(count_occurrences(numbers, number))