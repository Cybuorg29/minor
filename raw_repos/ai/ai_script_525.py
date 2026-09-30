def even_numbers():
    i = 0
    while True:
        if i % 2 == 0:
            yield i
        i += 1