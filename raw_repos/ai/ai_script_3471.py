def count_lines_of_code(code):
    lines = code.splitlines()
    return len(lines)

if __name__ == '__main__':
    code="""
def function(a, b):
    c = a + b
    d = a * b
    return c + d
    """
    print(count_lines_of_code(code))