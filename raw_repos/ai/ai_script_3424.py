def remove_words_by_letter(arr, letter):
  return [word for word in arr if letter not in word]

# Testing
arr = ["apple", "banana", "orange", "grape"]
filtered_arr = remove_words_by_letter(arr, 'a')
print("Filtered array: ", filtered_arr)