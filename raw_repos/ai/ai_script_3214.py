import re

def is_valid_email(email):
    regex = r"^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,6}$"
    if re.search(regex, email) is not None:
        return True
    else:
        return False

email = 'johnsmith@example.com'
if is_valid_email(email):
    print("Valid email")
else:
    print("Invalid email")