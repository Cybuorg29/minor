def find_non_repeating(array):
  for i in array:
    if array.count(i) == 1:
      return i
  
find_non_repeating(array); // Output: 1