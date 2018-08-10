traço = "-" * 30
nome = "Supermercado BARATÃO"
print(f"{traço}\n{nome:^30}\n{traço}")
print("\nDigite o nome do produto e seu valor.")
print("Quando terminar, digite sair para encerrar.")

lista = []
valid_nome = valid_preco = False
soma = 0
while True:
    while valid_nome == False:
        erros = 0
        prod = input("\nDigite o nome do produto:\n")
        prod_s = prod.split()
        for i in prod_s:
            if i.isalpha() == False:
                print("\nApenas letras são permitidas")
                erros += 1
        if erros == 0:
            valid_nome = True
    if prod == "sair" or prod == "Sair" or prod == "fechar" or prod == "Fechar":
        break
    while valid_preco == False:
        preço = input(f"Preço do(a){prod}: ")
        try:
            preço = float(preço)
            preço = round(preço, 2)
            soma += preço
            valid_preco = True
        except:
            print("\nDigite apenas números.")
    lista.append([prod, preço])
    valid_preco = False
    valid_nome = False

print()
print("-" * 31)
print(f"{nome:^31}")
print("-" * 31)
print(("PRODUTO".ljust(16)), ("VALOR"))
print("-" * 31)
for i in lista:
    print((f"{i[0]:19}").title() + (f"R$: {i[1]:>7}"))
total = "TOTAL:"
print()
print(f"{total:19}R$: {round(soma,2):>7}")
print("-" * 31)
print("Obrigado por comprar no BARATÂO\nVolte sempre!")
