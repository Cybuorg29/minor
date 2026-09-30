def check_brackets(bracket_string):
    """
    Function that checks if bracket string is correctly matched.
    """
    stack = []
    open_brackets = {'[', '{', '('}
    close_brackets = {']', '}', ')'}
    
    for bracket in bracket_string:
        if bracket in open_brackets:
            stack.append(bracket)
        elif bracket in close_brackets:
            if not stack or close_brackets[bracket] != stack.pop():
                return False
        
    return not stack