def find_closest_pair(points):
 min_dist = float('inf')
 closest_pair = None

 for i in range(len(points)):
 for j in range(i + 1, len(points)):
 dist = ((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)**0.5
 if dist < min_dist:
 min_dist = dist
 closest_pair = (points[i], points[j])
 
 return closest_pair