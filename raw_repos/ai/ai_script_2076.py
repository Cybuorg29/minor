def countQuadruplesSumZero(arr):
    """
    This function returns the number of quadruples that sum up to zero.
    """
    quad = 0
           
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            for k in range(j+1, len(arr)):
                for l in range(k+1, len(arr)):
                    if arr[i] + arr[j] + arr[k] + arr[l] == 0:
                        quad += 1
                            
    return quad