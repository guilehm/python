print('Bem-vindo à Mega Sena.')
input('Tecle enter para começar.')
print()
from random import randint

lista_sort = []
lista_esco = []
while len(lista_sort) < 6:
    x = int(randint(1,60))
    if x not in lista_sort:
        lista_sort.append(x)

while len(lista_esco) <6:
    x = input('Escolha um número:\n')
    try: 
        x = int(x)
        if x <1 or x > 60:
            print('\nEscolha números entre 1 e 60.')
        elif x in lista_esco:
            print('\nOs números não podem ser repetidos.')
        else:
            lista_esco.append(x)
    except: print('\nEscolha apenas números inteiros.')
    
lista_sort = sorted(lista_sort)
lista_esco = sorted(lista_esco)

print()
print('-'*52)
print('Os números sorteados foram: {}'.format(lista_sort))
print('Os números escolhidos foram: {}'.format(lista_esco))

lista_acert = []

for x in lista_esco:
    if x in lista_sort:
        lista_acert.append(x)

if len(lista_acert) >= 1:
    print('Os números acertados foram: {}'.format(lista_acert))
print('-'*52)

def acertos (x):
    return{
        0:'Você não acertou nenhum número.',
        1:'Você acertou apenas um.',
        2:'Você acertou dois números.',
        3:'Você acertou três números.',
        4:'Você acertou quatro números.',
        6:'Você acertou cinco números.',
        7:'Parabéns, você acertou a Mega Sena',
    }[x]

acertados = acertos(len(lista_acert))
print()
print(acertados)
