def test_sum(arr, sum): 
    for i in range(len(arr)-1): 
        for j in range(i+1, len(arr)): 
            if arr[i] + arr[j] == sum: 
                return True 
    return False

if __name__ == '__main__':
    arr = [1, 2, 3, 4] 
    sum = 7
    result = test_sum(arr, sum) 
    if result: 
        print("Array has two elements with the given sum") 
    else: 
        print("Array doesn't have two elements with the given sum")