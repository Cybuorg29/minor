import random

def generate_email():
 characters = 'abcdefghijklmnopqrstuvwxyz0123456789'
 email_address = ''.join(random.choice(characters) for i in range(10))
 return email_address + '@example.com'