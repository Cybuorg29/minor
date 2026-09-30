def first_last_words(arr):
    """Gets the first and last word from each string.
    
    Parameters:
    arr (list): array of strings
    """
    result = []
    for string in arr:
        words = string.split()
        result.append((words[0], words[-1]))
    return result

if __name__ == '__main__':
    array = ["Hello World", "Foo Bar", "Goodbye Moon"]
    print(first_last_words(array))