def is_prime(num):
  """Check if a number is a prime number."""
  if num <= 1:
    return False
  for i in range(2,num):
    if num % i == 0:
      return False
  return True