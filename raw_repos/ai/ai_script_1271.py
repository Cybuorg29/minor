def calculate_centroid(points): 
    n = len(points) 
  
    centroidX = sum(row[0] for row in points) / n
    centroidY = sum(row[1] for row in points) / n
     
    return [centroidX, centroidY] 
  
points = [(2, 3), (4, 7), (6, 9)] 
print(calculate_centroid(points))