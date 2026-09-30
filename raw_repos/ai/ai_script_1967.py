def cosine_distance(a, b):
  numerator = 0 
  sum_a_sq = 0 
  sum_b_sq = 0
  for (x, y) in zip(a, b):
    numerator += x*y
    sum_a_sq += x**2
    sum_b_sq += y**2
  
  denominator = (sum_a_sq * sum_b_sq)**.5
  return numerator/denominator

cosine_distance(vector1, vector2)