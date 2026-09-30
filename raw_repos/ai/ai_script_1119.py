def calculate_mean(arr):
    return sum(arr) / len(arr)
    
# Driver Code 
if __name__ == '__main__': 
    arr = [1, 2, 3, 4, 5]
    mean = calculate_mean(arr)
    print("Mean for given array is:", mean)