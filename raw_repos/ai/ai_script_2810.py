def format_phone_number(number):
    parts = number.split('-')
    digits = []
    for part in parts:
        for char in part:
            if char.isdigit():
                digits.append(char)
    return '+1' + ''.join(digits)

if __name__ == '__main__':
    number = '(123) 456-7890'
    canon_number = format_phone_number(number)
    print(canon_number)