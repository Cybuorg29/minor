import re

def validate_email(email):
    """Validates an email address using regex"""
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    match = re.search(pattern, email)
    if match:
        return True
    else:
        return False

email = 'example@gmail.com'

is_valid_email = validate_email(email)
print(is_valid_email) # Output: True