def herons_formula(lengths):
    a, b, c = lengths[0], lengths[1], lengths[2]
    s = (a + b + c) / 2
    area = (s*(s-a)*(s-b)*(s-c))** 0.5
    return area