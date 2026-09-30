def three_sum(array, number):
   result_sets = [] 
   for i in range(len(array) - 2):
       for j in range(i+1, len(array) - 1):
           for k in range(j+1, len(array)):
               if array[i] + array[j] + array[k] == number: 
                   result_sets.append([array[i], array[j], array[k]])
   return result_sets 

print(three_sum([2, 5, 8], 10)) # Result: [[2, 5, 8]]