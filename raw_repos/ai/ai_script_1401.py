def is_valid_sudoku(puzzle): 
  size = len(puzzle) 
  for row in range(len(puzzle)): 
    seen = set() 
    for col in range(size): 
      number = puzzle[row][col] 
      if number != 0: 
        if number in seen: 
          return False 
        seen.add(number) 
  for col in range(3): 
    seen = set() 
    for row in range(size): 
      number = puzzle[row][col] 
      if number != 0: 
        if number in seen: 
          return False 
        seen.add(number) 
  # and so on 
  return True