import re

def validate_string(input_str):
    pattern = r"\d"
    if re.search(pattern, input_str):
        return False
    else:
        return True