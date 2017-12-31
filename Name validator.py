valid_nome = False
while valid_nome == False:
    erros = 0
    nome = input('Digite seu nome:\n')
    nome_s = nome.split()
    for i in nome_s:
        if i.isalpha() == False:
            print('\nApenas letras são permitidas')
            erros += 1
    if erros == 0:
        valid_nome = True
print('Nome Validado com sucesso')
