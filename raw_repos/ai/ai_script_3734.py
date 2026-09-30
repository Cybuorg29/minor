def move_last_to_front(list):
  list[0], list[-1] = list[-1], list[0]
  return list