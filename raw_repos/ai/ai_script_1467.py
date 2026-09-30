def get_route_cost(distance_matrix,route):
    cost = 0
    for i in range(len(route)-1):
        cost += distance_matrix[route[i]][route[i+1]]
    return cost
  
route_cost = get_route_cost(distance_matrix, route) 
print (route_cost) 
# Output: 90