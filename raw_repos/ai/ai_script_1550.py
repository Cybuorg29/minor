def sum_areas(circles):
 total = 0
 for circle in circles:
 area = 3.14 * circle['radius'] ** 2
 total += area
 return total