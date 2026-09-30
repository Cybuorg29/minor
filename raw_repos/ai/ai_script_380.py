def get_roots_of_quad_eqn(a, b, c):
    # compute discriminant 
    d = (b**2) - (4 * a * c)
    
    # compute roots
    root1 = (-b + math.sqrt(d)) / (2 * a) 
    root2 = (-b - math.sqrt(d)) / (2 * a) 
    
    # return the roots
    return root1, root2

if __name__ == '__main__':
    a, b, c = 1, 4, 4
    print(get_roots_of_quad_eqn(a, b, c))