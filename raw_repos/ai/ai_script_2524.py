def authentication(role):
    if role == 'admin':
        return 'Admin privileges granted.'
    elif role == 'manager':
        return 'Manager privileges granted.'
    elif role == 'employee':
        return 'Employee privileges granted.'
    else:
        return 'Login failed. Invalid role.'