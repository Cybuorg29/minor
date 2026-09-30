def generate_non_unique_list(lst):
 new_list = []
 for i in lst:
  if lst.count(i) > 1 and i not in new_list:
   new_list.append(i)
 return new_list