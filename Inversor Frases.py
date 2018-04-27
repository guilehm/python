def inverter(frase):
    lista = []
    for i in range(len(frase)-1, -1, -1):
        lista.append(frase[i])
        print(i)
    print(lista)


frase = input('Digite uma frase:\n')

inverter(frase)