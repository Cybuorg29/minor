import numpy as np

def cosine_similarity(vector1, vector2):
    
    # normalize the vectors
    v1 = np.array(vector1)/np.linalg.norm(vector1)
    v2 = np.array(vector2)/np.linalg.norm(vector2)
    
    # calculate cosine similarity
    return np.dot(v1, v2) 
    
if __name__ == '__main__':
    vector1 = [1, 2, 3]
    vector2 = [4, 5, 6]
    print(cosine_similarity(vector1, vector2))