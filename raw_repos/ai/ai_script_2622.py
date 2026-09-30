def print_even(arr):
    even = []
    for num in arr:
        if num % 2 == 0:
            even.append(num)
    return even