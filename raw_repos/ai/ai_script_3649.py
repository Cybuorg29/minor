def my_generator(N):
    for i in range(N):
        yield i

g = my_generator(5)
print(list(g)) # [0, 1, 2, 3, 4]