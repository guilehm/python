def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

for x in range(10):
    print(fibonacci(x), end=" ")

print()
def fibonacci2(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
    return a

for x in range(10):
    print(fibonacci2(x), end=" ")