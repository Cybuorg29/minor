def binary_representation(num):
  if num > 1:
    binary_representation(num//2)
  print(num % 2, end = '')