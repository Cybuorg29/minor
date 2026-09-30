dictionary = {
 'level1': {
  'level2a': {
   'level3a': 1,
   'level3b': 3
  },
  'level2b': {
   'level3a': 4,
   'level3b': 5
  }
 }
}

def iterate_dict(d):
    result = 0
    for value in d.values():
        if type(value) is dict:
            result += iterate_dict(value)
        else:
            result += value
    return result

print(iterate_dict(dictionary)) # 13