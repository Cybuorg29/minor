def remove_duplicates(list):
 res = [] 
 for str in list:
 if str not in res:
 res.append(str)
 return res