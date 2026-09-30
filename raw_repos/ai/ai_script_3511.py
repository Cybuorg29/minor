def find_min(numbers):
  min_value = numbers[0]
  for n in numbers:
    if n < min_value:
      min_value = n
  
  return min_value
  
if __name__ == '__main__':
  numbers = [1, 15, 22, -5, 87]
  print(find_min(numbers))