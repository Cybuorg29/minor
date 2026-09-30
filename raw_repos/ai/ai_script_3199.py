def minkowski_distance(list_1, list_2, p):
    return (sum([abs(x-y)**p for x, y in zip(list_1, list_2)]))**(1/p)

# Result:
minkowski_distance(list_1, list_2, 3)  # 6.0