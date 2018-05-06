def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

for x in range(10):
    print(fibonacci(x), end=" ")