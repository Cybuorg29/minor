def processMatrix(matrix):
  result_matrix = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))] 
  for row in range(len(matrix)):
    for col in range(len(matrix[0])):
      element = matrix[row][col]
      # perform processing on element here
      result_matrix[row][col] = element
  return result_matrix