squares = [("{} ^2 = {}".format(a, a ** 2)) for a in range(1, 11)]
# print("".join(squares))

remainders = [i ** 2 % 15 for i in range(1, 51)]
# print(remainders)


table = ["{} x {} = {}".format(a, b, a * b) for a in range(1, 11) for b in range(1, 11)]
# print("\n".join(table))

lista = [
    "{},{},{}".format(a, b, c)
    for a in range(1, 4)
    for b in range(1, 4)
    for c in range(1, 4)
]
# print(']\n['.join(lista) + ']')

table2 = [
    "{:2} x {:2} = {:3}\n{}".format(a, b, a * b, ("-" * 13))
    if b == 10
    else "{:2} x {:2} = {:3}".format(a, b, a * b)
    for a in range(1, 11)
    for b in range(1, 11)
]
print("\n".join(table2))

numbers = [
    "{} ^ {} = {}".format(a, b, a ** b) for a in range(2, 6) for b in range(2, 6)
]
print("\n".join(numbers))
