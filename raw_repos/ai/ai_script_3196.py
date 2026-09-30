import re

# Validate the email address using the regex
email_pattern = re.compile(r'\S+@\S+\.\S+')
email_valid = re.match(email_pattern, email)

if email_valid:
    print("Valid Email Address")
else:
    print("Invalid Email Address")

# Output
Valid Email Address