import unicodedata

def string_to_unicode_array(string):
    return [unicodedata.lookup(ord(char)) for char in string]

if __name__ == '__main__':
    print(string_to_unicode_array('Hello World'))