def classifyList(lst):
    result = []
    for num in lst: 
        if num % 2 == 0: 
            result.append('even')
        else:
            result.append('odd')
    return result