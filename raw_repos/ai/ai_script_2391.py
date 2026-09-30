def string_to_dict(string):
    data = string.split(' ') 
    answer = dict() 
    for element in data: 
        if element in answer: 
            answer[element] += 1
        else: 
            answer[element] = 1
    return answer