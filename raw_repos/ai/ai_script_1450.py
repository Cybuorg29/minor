def compare_strings(string_1, string_2):
    similarity_score = 0
    n = min(len(string_1), len(string_2))
    for i in range(n): 
        if string_1[i] == string_2[i]: 
            similarity_score += 1
    return similarity_score