# primeira forma
def fatoracao(num):
    if num == 0 or num ==1:
        return 1
    else:
        result = num
        while num > 1:
            result = result * (num-1)
            num -= 1
        return result

num = int(input('Insira um número: '))
print('F1', fatoracao(num))


# segunda forma
def fatoracao_2(num):
    fat = 1
    for i in range(2, (num + 1)):
        fat *= num
        num -=1
    return fat

fatoracao2 = fatoracao_2(num)
print('F2', fatoracao2)

# terceira forma
def fatoracao_3(num):
    f = 1
    while num > 1:
        f *= num
        num -= 1
    return f

fatoracao3 = fatoracao_3(num)
print('F3', fatoracao3)


# recursivo
def fatorial_4(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial_4(n - 1)

fatoracao4 = fatorial_4(num)
print('F4', fatoracao4)
