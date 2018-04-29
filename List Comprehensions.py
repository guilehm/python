squares = ([('{} ^2 = {}'.format(a, a**2)) for a in range(1,11)])
print(squares)

remainders = [i**2 % 5 for i in range(1,101)]
print(remainders)
