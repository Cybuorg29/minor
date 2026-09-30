def generate_password():
    """Generate a random password of 8 characters."""
    import random
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'
    password = ''
    for i in range(8):
        password += random.SystemRandom().choice(chars)
    return password