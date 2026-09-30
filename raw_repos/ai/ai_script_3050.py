def is_power_of_3(num):
  if num == 1:
    return True
  elif num % 3 != 0:
    return False
  else:
    return is_power_of_3(num / 3)