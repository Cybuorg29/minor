def sort_list(numbers):
    #Base case
    if len(numbers) <= 1:
        return numbers

    pivot = numbers[0]
    left = []
    right = []
    #Divide
    for num in numbers[1:]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)
    #Conquer
    left = sort_list(left)
    right = sort_list(right)
    #Combine
    return left + [pivot] + right

if __name__ == '__main__':
    arr = [7, 3, 1, 9, 0]
    print(sort_list(arr))