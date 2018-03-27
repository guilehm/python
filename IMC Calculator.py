print('Este programa irá calcular o seu IMC.')
print('Faremos algumas perguntas para obtenção do resultado.')
print()

# validar sexo
valid_sexo = False
while valid_sexo == False:
    sexo = input('Informe o sexo com M ou F:\n').lower()
    if sexo == 'm':
        valid_sexo = True
    elif sexo == 'f':
        valid_sexo = True
    else:
        print('Informe o sexo corretamente.')
        print()

# validar peso
valid_peso = False
while valid_peso == False:
    peso = input("Informe o peso:\n")
    try:
        peso = float(peso)
        valid_peso = True
    except:
        print('Digite o peso corretamente.\nUtilize apenas numeros e separe a casa decimal com ponto.\nNão é necessário digitar "kg"')
        print()

# validar altura
valid_altura = False
while valid_altura == False:
    altura = input('Informe a altura:\n')
    try:
        altura = float(altura)
        valid_altura = True
    except:
        print('Digite a altura corretamente.\nUtilize apenas numeros e separe a casa decimal com ponto.')
        print()
        
if sexo == 'm':
    sexo = 'masculino'
else:
    sexo='feminino'
        
print('O sexo é {}, o peso é {}kg e a altura é {}m.'.format(sexo, peso, altura))


# função para calculos
def imc(peso,altura):
    indice_massa = (peso / (altura*altura))
    return(indice_massa)

if sexo == 'masculino':
    if imc(peso,altura)>=31.1:
        print('Você tá gordão!')
    elif imc(peso,altura)>=27.8:
        print('Acima do peso ideal')
    elif imc(peso,altura)>=26.4:
        print('Marginalmente acima do peso')
    elif imc(peso,altura)>=20.7:
        print('No peso normal')
    elif imc(peso,altura)<20.7:
        print('Abaixo do peso')
    else:
        print('Ocorreu um erro')
if sexo == 'feminino':
    if imc(peso,altura)>=32.3:
        print('Você tá gordona!')
    elif imc(peso,altura)>=27.3:
        print('Acima do peso ideal')
    elif imc(peso,altura)>=25.8:
        print('Marginalmente acima do peso')
    elif imc(peso,altura)>=19.1:
        print('No peso normal')
    elif imc(peso,altura)<19.1:
        print('Abaixo do peso')
    else:
        print('Ocorreu um erro')

input('Tecle enter para sair')
