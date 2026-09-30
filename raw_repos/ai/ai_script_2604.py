def is_algorithm_syntactically_correct(algorithm):
    algorithm = algorithm.replace('\n', ' ').replace('\t ', ' ').lower()
    
    required_words = ['read', 'input', 'initialize', 'variables', 'process', 'output', 'result']
    for word in required_words:
        if word not in algorithm:
            return False
    return True