def pairs_with_sum(arr, value):
    pairs = []
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if (arr[i] + arr[j] == value):
                pairs.append((arr[i], arr[j]))
    return pairs