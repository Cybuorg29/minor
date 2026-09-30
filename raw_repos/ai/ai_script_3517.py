def get_even_numbers(numbers):
  even_numbers = []
  for num in numbers:
    if num % 2 == 0:
      even_numbers.append(num)
  return even_numbers

if __name__ == "__main__":
  print("Even numbers from original list:", get_even_numbers(numbers))