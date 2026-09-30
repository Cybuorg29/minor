import re

def find_capital_letter(text):
    pattern = r"[A-Z]"
    result = re.findall(pattern, text)
    return result[0]

print(find_capital_letter(text))