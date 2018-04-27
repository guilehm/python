from random import sample

options = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
qtd = 100
while qtd > 74:
    qtd = int(input('Digite a quantidade de caracteres:\n'))
    if qtd > 74:
        print('\nQuantidade de caracteres inválida.')

print('Sua senha é:\n' + "".join(sample(options, qtd)))
