"""
Create a function that can concatenate two lists into a string separated by comma
"""
def concat_lists(list1, list2):
  return ','.join([str(i) for i in list1 + list2]) 
  
if __name__ == '__main__':
    print(concat_lists([1, 2, 3], [4, 5, 6]))