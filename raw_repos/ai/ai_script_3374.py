def delete(A, B):
    for i in B:
        if i in A:
            A = A.replace(i, '')
    return A

delete(A, B) # Output: 'bdef'