def validate_phone(phone_number):
    regex = '^\+?(\d[\d-. ]+)?(\([\d-. ]+\))?[\d-. ]+\d$'
    if re.match(regex, phone_number):
        return True
    return False