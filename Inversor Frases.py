def inverter(frase):
    lista = []
    for i in range(len(frase)-1, -1, -1):
        lista.append(frase[i])
    lista = "".join(lista)
    print(lista)


frase = input('Digite uma frase:\n')

inverter(frase)
