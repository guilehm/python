num = int(input('Digite o valor do seu saque: '))
notas_50 = notas_20 = notas_10 = notas_1 = 0

if num >= 50:
    notas_50 = num // 50
    num = num % 50
if num >= 20:
    notas_20 = num // 20
    num = num % 20
if num >= 10:
    notas_10 = num // 10
    num = num % 10
if num > 0:
    notas_1 = num // 1
    num = num % 1


if notas_50: print('Notas 50: {}'.format(notas_50))
if notas_20: print('Notas 20: {}'.format(notas_20))
if notas_10: print('Notas 10: {}'.format(notas_10))
if notas_1: print('Notas 1: {}'.format(notas_1))

