def delete_duplicates(arr)
  arr.uniq
end
 
arr = [1,2,2,3,3,4,5]
new_arr = delete_duplicates(arr)
p new_arr # => [1, 2, 3, 4, 5]