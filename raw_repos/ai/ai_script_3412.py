def max_product_three_numbers(arr):
    arr.sort()
    return max(arr[-1] * arr[-2] * arr[-3], arr[0] * arr[1] * arr[-1])

max_product = max_product_three_numbers([-1, -2, 4, 5, 8, 9])
print(max_product)  # Output: 360