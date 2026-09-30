def print_fibonacci(n):
  a = 0
  b = 1
  print('Fibonacci sequence:')
  while a < n:
    print(a, end=' ')
    tmp_var = a
    a = b
    b = tmp_var + b

num = int(input("Enter positive number: "))
print_fibonacci(num)