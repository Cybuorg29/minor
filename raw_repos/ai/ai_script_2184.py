def cosine_similarity(v1, v2):
    dot = 0
    mag1 = 0
    mag2 = 0
    for a, b in zip(v1, v2):
        dot += a*b
        mag1 += a**2
        mag2 += b**2
    return dot/(mag1**0.5 * mag2**0.5)

v1 = [2, 3]
v2 = [4, -5]

cosine_sim = cosine_similarity(v1, v2)

print(cosine_sim)