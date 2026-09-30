def findMaxDepth(dict_):
   max_depth = 1
   for val in dict_.values():
      if isinstance(val, dict):
         max_depth = max(max_depth, 1 + findMaxDepth(val))
   return max_depth

findMaxDepth(dict) // 3