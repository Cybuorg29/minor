"""
Write a code to output a substring of the given string
"""

def substring(inp_str, start, end):
    return inp_str[start:end]

if __name__ == '__main__':
    inp_str = "Hello World" 
    start = 3
    end = 5
    print(substring(inp_str, start, end))