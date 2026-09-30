def remove_duplicates(arr) 
  arr.uniq 
end 
  
puts remove_duplicates([1, 2, 2, 3, 4, 4]) # should print [1, 2, 3, 4]