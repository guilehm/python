def generator():
    # yield 1
    for i in range(2, 5):
        yield i

g = generator()
print(next(g))
print(next(g))
print(next(g))
print('')

def generator_2():
    for i in range(10):
        yield i

g2 = generator_2()
print(next(g2))
print(next(g2))
print(next(g2))
print(next(g2))
print(next(g2))
