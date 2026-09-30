def create_buckets(arr):
    buckets = []
    x = arr[0]
    for i in range(1, len(arr)):
        if arr[i] != x + 1:
            buckets.append(arr[i-1])
            x = arr[i]
    buckets.append(arr[-1])
    return buckets

create_buckets([2, 3, 6, 7, 8])
# Output: [2, 3, 6, 8]