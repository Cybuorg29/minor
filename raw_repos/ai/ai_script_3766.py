def avg(arr): 
    sum = 0 
    for num in arr:
        sum += num 
    return sum/len(arr)  
  
numbers = [3, 7, 11, 15]
average = avg(numbers) 
print("Average of the numbers:",average)  // Output: 9.5