squares = ([('{} ^2 = {}'.format(a, a**2)) for a in range(1,11)])
print(squares)

remainders = [i**2 % 15 for i in range(1,51)]
print(remainders)

table = ['{} x {} = {}'.format(a, b, a*b) for a in range(1,11) for b in range(1,11)]
print(table)