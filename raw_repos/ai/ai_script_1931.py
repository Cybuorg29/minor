def largest_string(array):
   largest_string=array[0]
   for i in array:
      if len(i) > len(largest_string):
         largest_string = i
   return largest_string