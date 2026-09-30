"""
Create a function that can tranform a string of text into an object containing the number of occurrences of each letter in the string
"""
def count_letters(s):
  letter_dict = {}
  for letter in s:
    if letter in letter_dict:
      letter_dict[letter] += 1
    else:
      letter_dict[letter] = 1
  
  return letter_dict

if __name__ == '__main__':
    print(count_letters('Hello World')) # {'H': 1, 'e': 1, 'l': 3, 'o': 2, 'W': 1, 'r': 1, 'd': 1}