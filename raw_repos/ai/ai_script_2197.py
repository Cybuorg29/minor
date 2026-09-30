def find_elements(list, number): 
    result = [] 
    for i in range(len(list)): 
        for j in range(i + 1, len(list)): 
            if list[i] + list[j] == number: 
                result.append([list[i], list[j]]) 
  
    return result 
  
# Driver code 
list = [5, 7, 9, 4] 
n = 18
print(find_elements(list, n))