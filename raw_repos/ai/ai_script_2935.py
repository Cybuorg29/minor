def add_vectors(v1, v2):
    result = []
    for i in range(len(v1)):
        result.append(v1[i] + v2[i])
    return result
 
print(add_vectors([3, 4], [5, 6]))