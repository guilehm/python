from random import choice, randint, uniform
from time import sleep

print('-' * 26)
print(('Bem-vindo ao jogo Combate!').upper())
print('-' * 26)

valid_nome = False
while valid_nome == False:  # validação do nome
    nome1 = input('Informe seu nome para começar:\n').title()
    if nome1.isalpha():
        if len(nome1) >= 3 and len(nome1) <= 20:
            valid_nome = True
        else:
            print('\nO nome precisa ter em 3 e 20 caracteres.')
    else:
        print('\nApenas letras são permitidas para nome.')

lista_nomes = [
    'Jurema',
    'Tainara',
    'João',
    'Morgana',
    'Denilson',
    'Marcia',
    'Janaína',
    'Anor',
    'Jean',
    'Juverci',
    'Ezequiel',
    'Ester',
    'Diego',
    'Ilza',
    'Gilberto',
    'Geraldo',
    'Creuza',
    'Joaquim',
    'Simone',
    'Marcelo',
    'Josevaldo',
    'Claudinei',
    'Meire',
    'Romário',
    'Geralda',
    'Manoel',
    'Maurílio',
    'José',
    'Silvano',
    'Ambrósio',
    'Deuzivaldo',
    'Joacir',
    'Juvenalda',
    'Gildeci',
    'José Mauro',
    'José Geraldo',
    'Zélia',
    'Shirlei',
    'Adão',
    'Irineu',
    'Jadel',
]

jogador1 = {'Nome': nome1, 'Vitalidade': 100, 'Ataque': 100, 'Defesa': 100}
jogador2 = {
    'Nome': choice(lista_nomes),
    'Vitalidade': 100,
    'Ataque': 100,
    'Defesa': 100,
}

# definição de variáveis para simplificar a busca de informações
nome1 = jogador1['Nome']
vida1 = round(jogador1['Vitalidade'], 2)
atk1 = jogador1['Ataque']
def1 = jogador1['Defesa']

nome2 = jogador2['Nome']
vida2 = round(jogador2['Vitalidade'], 2)
atk2 = jogador2['Ataque']
def2 = jogador2['Defesa']


print('\nOlá, {}, seja bem-vindo(a).'.format(nome1))
input('O nome de seu oponente é {}.'.format(nome2))
input('\nO jogo termina quando um jogador morrer, ou quando você encerrar o turno.')


def calcula_Soco(x):
    dano = x * 4.5 * uniform(0.9, 1.0)
    dano /= 32
    red = randint(0, 4)
    vit = 1
    return [int(dano), red, vit]


def calcula_Chute(x):
    dano = x * 5.0 * uniform(0.9, 1.1)
    dano /= 32
    red = randint(2, 5)
    vit = 3
    return [int(dano), red, vit]


def calcula_Voadora(x):
    dano = x * 5.3 * uniform(0.8, 1.2)
    dano /= 32
    red = randint(5, 7)
    vit = randint(3, 5)
    return [int(dano), red, vit]


def calcula_Flecha(x):
    dano = x * 5.8 * uniform(0.7, 1.5)
    dano /= 32
    red = randint(7, 9)
    vit = 0
    return [int(dano), red, vit]


def calcula_Espada(x):
    dano = x * 6.2 * uniform(0.9, 1.4)
    dano /= 32
    red = randint(7, 12)
    vit = randint(11, 15)
    return [int(dano), red, vit]


###### ataque do player ######
def soco(x):
    ataque = calcula_Soco(x)  # chamar função de ataque
    dano, p_atb, p_vit = (
        ataque[0],
        ataque[1],
        ataque[2],
    )  # atribui retorno da função às variáveis dano e atb(atk, def)
    dano = round(
        (dano / (1 + (jogador2['Defesa'] / 100)) + dano / 2), 2
    )  # cálculo de redução de dano por escudo
    jogador2['Vitalidade'] -= dano  # reduz a vitalidade o valor do dano no defensor
    jogador2['Defesa'] -= p_atb + 3  # reduz a defesa com incremento de 3 no defensor
    jogador1['Ataque'] -= p_atb  # reduz o ataque no atacante
    jogador1['Vitalidade'] -= p_vit  # reduz a vitalidade no atacante
    sleep(1)
    print('\n{} enche a mão e acerta um soco em {}.'.format(nome1, nome2))
    sleep(2)
    print(
        '{} perdeu {}PV devido ao soco efetuado por {}.'.format(
            jogador2['Nome'], dano, jogador1['Nome']
        )
    )
    sleep(2)
    print('{} perde {} de defesa.'.format(jogador2['Nome'], p_atb + 3))
    sleep(2)
    print('{} perde {} de ataque.'.format(jogador1['Nome'], p_atb))
    sleep(2)
    print('{} perde {} de vitalidade.'.format(jogador1['Nome'], p_vit))
    sleep(2)


def chute(x):
    ataque = calcula_Chute(x)  # chamar função de ataque
    dano, p_atb, p_vit = (
        ataque[0],
        ataque[1],
        ataque[2],
    )  # atribui retorno da função às variáveis dano e atb(atk, def)
    dano = round(
        (dano / (1 + (jogador2['Defesa'] / 100)) + dano / 2), 2
    )  # cálculo de redução de dano por escudo
    jogador2['Vitalidade'] -= dano  # reduz a vitalidade o valor do dano no defensor
    jogador2['Defesa'] -= p_atb + 3  # reduz a defesa com incremento de 3 no defensor
    jogador1['Ataque'] -= p_atb  # reduz o ataque no atacante
    jogador1['Vitalidade'] -= p_vit  # reduz a vitalidade no atacante
    sleep(1)
    print('\n{} prepara a canela e acerta um chute em {}.'.format(nome1, nome2))
    sleep(2)
    print(
        '{} perdeu {}PV devido ao chute efetuado por {}.'.format(
            jogador2['Nome'], dano, jogador1['Nome']
        )
    )
    sleep(2)
    print('{} perde {} de defesa.'.format(jogador2['Nome'], p_atb + 3))
    sleep(2)
    print('{} perde {} de ataque.'.format(jogador1['Nome'], p_atb))
    sleep(2)
    print('{} perde {} de vitalidade.'.format(jogador1['Nome'], p_vit))
    sleep(2)


def voadora(x):
    ataque = calcula_Voadora(x)  # chamar função de ataque
    dano, p_atb, p_vit = (
        ataque[0],
        ataque[1],
        ataque[2],
    )  # atribui retorno da função às variáveis dano e atb(atk, def)
    dano = round(
        (dano / (1 + (jogador2['Defesa'] / 100)) + dano / 2), 2
    )  # cálculo de redução de dano por escudo
    jogador2['Vitalidade'] -= dano  # reduz a vitalidade o valor do dano no defensor
    jogador2['Defesa'] -= p_atb + 3  # reduz a defesa com incremento de 3 no defensor
    jogador1['Ataque'] -= p_atb  # reduz o ataque no atacante
    jogador1['Vitalidade'] -= p_vit  # reduz a vitalidade no atacante
    sleep(1)
    print(
        '\n{} sai correndo e acerta uma voadora nas costas de {}.'.format(nome1, nome2)
    )
    sleep(2)
    print(
        '{} perdeu {}PV devido a voadora efetuada por {}.'.format(
            jogador2['Nome'], dano, jogador1['Nome']
        )
    )
    sleep(2)
    print('{} perde {} de defesa.'.format(jogador2['Nome'], p_atb + 3))
    sleep(2)
    print('{} perde {} de ataque.'.format(jogador1['Nome'], p_atb))
    sleep(2)
    print('{} perde {} de vitalidade.'.format(jogador1['Nome'], p_vit))
    sleep(2)


def flecha(x):
    ataque = calcula_Flecha(x)  # chamar função de ataque
    dano, p_atb, p_vit = (
        ataque[0],
        ataque[1],
        ataque[2],
    )  # atribui retorno da função às variáveis dano e atb(atk, def)
    dano = round(
        (dano / (1 + (jogador2['Defesa'] / 100)) + dano / 2), 2
    )  # cálculo de redução de dano por escudo
    jogador2['Vitalidade'] -= dano  # reduz a vitalidade o valor do dano no defensor
    jogador2['Defesa'] -= p_atb + 3  # reduz a defesa com incremento de 3 no defensor
    jogador1['Ataque'] -= p_atb  # reduz o ataque no atacante
    jogador1['Vitalidade'] -= p_vit  # reduz a vitalidade no atacante
    sleep(1)
    print('\n{} prepara o arco, mira e acerta uma flecha em {}.'.format(nome1, nome2))
    sleep(2)
    print(
        '{} perdeu {}PV devido a flecha disparada por {}.'.format(
            jogador2['Nome'], dano, jogador1['Nome']
        )
    )
    sleep(2)
    print('{} perde {} de defesa.'.format(jogador2['Nome'], p_atb + 3))
    sleep(2)
    print('{} perde {} de ataque.'.format(jogador1['Nome'], p_atb))
    sleep(2)
    print('{} perde {} de vitalidade.'.format(jogador1['Nome'], p_vit))
    sleep(2)


def espada(x):
    ataque = calcula_Espada(x)  # chamar função de ataque
    dano, p_atb, p_vit = (
        ataque[0],
        ataque[1],
        ataque[2],
    )  # atribui retorno da função às variáveis dano e atb(atk, def)
    dano = round(
        (dano / (1 + (jogador2['Defesa'] / 100)) + dano / 2), 2
    )  # cálculo de redução de dano por escudo
    jogador2['Vitalidade'] -= dano  # reduz a vitalidade o valor do dano no defensor
    jogador2['Defesa'] -= p_atb + 3  # reduz a defesa com incremento de 3 no defensor
    jogador1['Ataque'] -= p_atb  # reduz o ataque no atacante
    jogador1['Vitalidade'] -= p_vit  # reduz a vitalidade no atacante
    sleep(1)
    print('\n{} desembainha a espada e ataca {}.'.format(nome1, nome2))
    sleep(2)
    print(
        '{} perdeu {}PV devido ao ataque de espada efetuado por {}.'.format(
            jogador2['Nome'], dano, jogador1['Nome']
        )
    )
    sleep(2)
    print('{} perde {} de defesa.'.format(jogador2['Nome'], p_atb + 3))
    sleep(2)
    print('{} perde {} de ataque.'.format(jogador1['Nome'], p_atb))
    sleep(2)
    print('{} perde {} de vitalidade.'.format(jogador1['Nome'], p_vit))
    sleep(2)


###### fim atq do player ######

###### ataque do bot ######


def soco2(x):
    ataque = calcula_Soco(x)  # chamar função de ataque
    dano, p_atb, p_vit = (
        ataque[0],
        ataque[1],
        ataque[2],
    )  # atribui retorno da função às variáveis dano e atb(atk, def)
    dano = round(
        (dano / (1 + (jogador1['Defesa'] / 100)) + dano / 2), 2
    )  # cálculo de redução de dano por escudo
    jogador1['Vitalidade'] -= dano  # reduz a vitalidade o valor do dano no defensor
    jogador1['Defesa'] -= p_atb + 3  # reduz a defesa com incremento de 3 no defensor
    jogador2['Ataque'] -= p_atb  # reduz o ataque no atacante
    jogador2['Vitalidade'] -= p_vit  # reduz a vitalidade no atacante
    sleep(1)
    print('\n{} vem de mão fechada e mete um soco em {}.'.format(nome2, nome1))
    sleep(2)
    print(
        '{} perdeu {}PV devido ao soco efetuado por {}.'.format(
            jogador1['Nome'], dano, jogador2['Nome']
        )
    )
    sleep(2)
    print('{} perde {} de defesa.'.format(jogador1['Nome'], p_atb + 3))
    sleep(2)
    print('{} perde {} de ataque.'.format(jogador2['Nome'], p_atb))
    sleep(2)
    print('{} perde {} de vitalidade.'.format(jogador2['Nome'], p_vit))
    sleep(2)


def chute2(x):
    ataque = calcula_Chute(x)  # chamar funcao de ataque
    dano, p_atb, p_vit = (
        ataque[0],
        ataque[1],
        ataque[2],
    )  # atribui retorno da função às variáveis dano e atb(atk, def)
    dano = round(
        (dano / (1 + (jogador1['Defesa'] / 100)) + dano / 2), 2
    )  # cálculo de redução de dano por escudo
    jogador1['Vitalidade'] -= dano  # reduz a vitalidade o valor do dano no defensor
    jogador1['Defesa'] -= p_atb + 3  # reduz a defesa com incremento de 3 no defensor
    jogador2['Ataque'] -= p_atb  # reduz o ataque no atacante
    jogador2['Vitalidade'] -= p_vit  # reduz a vitalidade no atacante
    sleep(1)
    print('\n{} mete uma bicuda em {}.'.format(nome2, nome1))
    sleep(2)
    print(
        '{} perdeu {}PV devido ao chute efetuado por {}.'.format(
            jogador1['Nome'], dano, jogador2['Nome']
        )
    )
    sleep(2)
    print('{} perde {} de defesa.'.format(jogador1['Nome'], p_atb + 3))
    sleep(2)
    print('{} perde {} de ataque.'.format(jogador2['Nome'], p_atb))
    sleep(2)
    print('{} perde {} de vitalidade.'.format(jogador2['Nome'], p_vit))
    sleep(2)


def voadora2(x):
    ataque = calcula_Voadora(x)  # chamar função de ataque
    dano, p_atb, p_vit = (
        ataque[0],
        ataque[1],
        ataque[2],
    )  # atribui retorno da função às variáveis dano e atb(atk, def)
    dano = round(
        (dano / (1 + (jogador1['Defesa'] / 100)) + dano / 2), 2
    )  # cálculo de redução de dano por escudo
    jogador1['Vitalidade'] -= dano  # reduz a vitalidade o valor do dano no defensor
    jogador1['Defesa'] -= p_atb + 3  # reduz a defesa com incremento de 3 no defensor
    jogador2['Ataque'] -= p_atb  # reduz o ataque no atacante
    jogador2['Vitalidade'] -= p_vit  # reduz a vitalidade no atacante
    sleep(1)
    print('\n{} vai com os dois pés na cabeça de {}.'.format(nome2, nome1))
    sleep(2)
    print(
        '{} perdeu {}PV devido a voadora efetuada por {}.'.format(
            jogador1['Nome'], dano, jogador2['Nome']
        )
    )
    sleep(2)
    print('{} perde {} de defesa.'.format(jogador1['Nome'], p_atb + 3))
    sleep(2)
    print('{} perde {} de ataque.'.format(jogador2['Nome'], p_atb))
    sleep(2)
    print('{} perde {} de vitalidade.'.format(jogador2['Nome'], p_vit))
    sleep(2)


def flecha2(x):
    ataque = calcula_Flecha(x)  # chamar função de ataque
    dano, p_atb, p_vit = (
        ataque[0],
        ataque[1],
        ataque[2],
    )  # atribui retorno da função às variáveis dano e atb(atk, def)
    dano = round(
        (dano / (1 + (jogador1['Defesa'] / 100)) + dano / 2), 2
    )  # cálculo de redução de dano por escudo
    jogador1['Vitalidade'] -= dano  # reduz a vitalidade o valor do dano no defensor
    jogador1['Defesa'] -= p_atb + 3  # reduz a defesa com incremento de 3 no defensor
    jogador2['Ataque'] -= p_atb  # reduz o ataque no atacante
    jogador2['Vitalidade'] -= p_vit  # reduz a vitalidade no atacante
    sleep(1)
    print(
        '\n{} pega seu arco e acerta uma flecha na cabeça de {}.'.format(nome2, nome1)
    )
    sleep(2)
    print(
        '{} perdeu {}PV devido a flecha disparada por {}.'.format(
            jogador1['Nome'], dano, jogador2['Nome']
        )
    )
    sleep(2)
    print('{} perde {} de defesa.'.format(jogador1['Nome'], p_atb + 3))
    sleep(2)
    print('{} perde {} de ataque.'.format(jogador2['Nome'], p_atb))
    sleep(2)
    print('{} perde {} de vitalidade.'.format(jogador2['Nome'], p_vit))
    sleep(2)


def espada2(x):
    ataque = calcula_Espada(x)  # chamar função de ataque
    dano, p_atb, p_vit = (
        ataque[0],
        ataque[1],
        ataque[2],
    )  # atribui retorno da função às variáveis dano e atb(atk, def)
    dano = round(
        (dano / (1 + (jogador1['Defesa'] / 100)) + dano / 2), 2
    )  # cálculo de redução de dano por escudo
    jogador1['Vitalidade'] -= dano  # reduz a vitalidade o valor do dano no defensor
    jogador1['Defesa'] -= p_atb + 3  # reduz a defesa com incremento de 3 no defensor
    jogador2['Ataque'] -= p_atb  # reduz o ataque no atacante
    jogador2['Vitalidade'] -= p_vit  # reduz a vitalidade no atacante
    sleep(1)
    print('\n{} acerta a espada em {}.'.format(nome2, nome1))
    sleep(2)
    print(
        '{} perdeu {}PV devido ao ataque de espada efetuado por {}.'.format(
            jogador1['Nome'], dano, jogador2['Nome']
        )
    )
    sleep(2)
    print('{} perde {} de defesa.'.format(jogador1['Nome'], p_atb + 3))
    sleep(2)
    print('{} perde {} de ataque.'.format(jogador2['Nome'], p_atb))
    sleep(2)
    print('{} perde {} de vitalidade.'.format(jogador2['Nome'], p_vit))
    sleep(2)


###### fim atq do bot ######

repet_atk = True
prox_turn = False
encerrar = False

while repet_atk == True and encerrar == False:
    while prox_turn == False and encerrar == False:
        tipo_atk = input(
            '\nEscolha o tipo de ataque.\nPara mais informações digite "info" ou "stats".\nAtaque: '
        ).lower()
        if tipo_atk == 'soco' or tipo_atk == 's':
            atacar = soco(atk1)
            prox_turn = True
        elif tipo_atk == 'chute' or tipo_atk == 'c':
            atacar = chute(atk1)
            prox_turn = True
        elif tipo_atk == 'voadora' or tipo_atk == 'v':
            atacar = voadora(atk1)
            prox_turn = True
        elif tipo_atk == 'flecha' or tipo_atk == 'f':
            atacar = flecha(atk1)
            prox_turn = True
        elif tipo_atk == 'espada' or tipo_atk == 'e':
            atacar = espada(atk1)
            prox_turn = True
        elif tipo_atk == 'sair':
            repet_atk = False
        elif tipo_atk == 'info':
            input(
                '\nATAQUES DISPONÍVEIS:\nSoco, Chute, Voadora, Flecha e Espada.\nCada ataque efetuado causará dano em seu oponente, ataques mais fortes possuem maiores penalidades.\nO cálculo do dano é feito baseado no tipo de ataque, na força do atacante e na força de defesa do defensor.\nOu para sair digite "sair".'
            )
        elif tipo_atk == 'stats':
            print('\nSTATUS DOS JOGADORES:')
            print(
                '{}: {} de vitalidade, {} Ataque e {} Defesa.'.format(
                    nome1, vida1, atk1, def1
                )
            )
            print(
                '{}: {} de vitalidade, {} Ataque e {} Defesa.'.format(
                    nome2, vida2, atk2, def2
                )
            )
        else:
            print('\nEscolha um ataque válido.')

    if jogador1['Vitalidade'] <= 0 or jogador2['Vitalidade'] <= 0:
        encerrar = True

    while prox_turn == True and encerrar == False:
        input(
            '\nAgora é a vez de {} atacar.\nQuando estiver pronto para defender, tecle ENTER.'.format(
                nome2
            )
        )
        escolha = randint(1, 7)
        if escolha == 1:
            atacar = soco2(atk2)
            prox_turn = False
        elif escolha == 2:
            atacar = chute2(atk2)
            prox_turn = False
        elif escolha == 3:
            atacar = voadora2(atk2)
            prox_turn = False
        elif escolha == 4 or escolha == 5:
            atacar = flecha2(atk2)
            prox_turn = False
        elif escolha == 6 or escolha == 7:
            atacar = espada2(atk2)
            prox_turn = False

        print('\nFim do turno.')
        result = input(
            'Digite "resultado" para ver o resultado do turno ou pressione ENTER para continuar.'
        ).lower()
        if result == 'resultado' or result == 'r':
            print('{}:'.format(nome1))
            print(
                '{} PV, {} Ataque {} Defesa.'.format(
                    round(jogador1['Vitalidade'], 2),
                    jogador1['Ataque'],
                    jogador1['Defesa'],
                )
            )
            print('{}:'.format(nome2))
            print(
                '{} PV, {} Ataque {} Defesa.'.format(
                    round(jogador2['Vitalidade'], 2),
                    jogador2['Ataque'],
                    jogador2['Defesa'],
                )
            )
        if jogador1['Vitalidade'] <= 0 or jogador2['Vitalidade'] <= 0:
            encerrar = True
        if result == 'resultado' or result == 'r':
            resp = input(
                '\nTecle ENTER para ir ao próximo turno ou digite "Sair" para terminar o combate.'
            ).lower()
        if result == 'sair' or result == 's':
            prox_turn = False
            repet_atk = False

print('\nFIM DE JOGO')
if jogador1['Vitalidade'] > jogador2['Vitalidade']:
    print(nome2, 'perdeu e o vencedor foi:')
else:
    print(nome1, 'perdeu e o vencedor foi:')
print('-' * 20)

if jogador1['Vitalidade'] > jogador2['Vitalidade']:
    print(nome1.upper())
else:
    print(nome2.upper())
print('-' * 20)
