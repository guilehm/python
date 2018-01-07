from random import randint, uniform


class Personagem():
    def __init__(self, nome, vida, p_ataque, p_defesa):  # definir características dos personagens
        self.nome = nome
        self.vida = vida
        self.p_ataque = p_ataque
        self.p_defesa = p_defesa
        self.vivo = True

    def carac(self):  # imprimir stats
        print(f'Nome do personagem: {self.nome}')
        print(f'HP: {self.vida:.2f}')
        print(f'PA: {self.p_ataque}')
        print(f'PD: {self.p_defesa}\n')

    def hp(self):  # imprimir hp
        print('{}'.format(self.nome).upper())
        print(f'HP: {self.vida:.2f}')

    def ataque(self, object, x=100):
        cont = 1
        while self.vivo is True and object.vivo is True and cont <= x:  # loop para ninguém atacar mortos
            if self.vivo is True and object.vivo is True:  # se está vivo, ataca
                self.dano = (self.p_ataque / 4) * uniform(0.8, 1.2)
                defesa = (object.p_defesa) * 0.1
                self.dano = self.dano - defesa
                object.vida = (object.vida) - self.dano
                if object.vida <= 0:  # se morreu
                    object.vida = 0
                    object.vivo = False
                    print(f'\n{self.nome} derrota {object.nome} com um dano de: {self.dano:.2f}.')
                else:
                    print(f'{self.nome} ataca {object.nome} e inflige: {self.dano:.2f}.')
            if object.vivo is True and self.vivo is True:
                object.dano = (object.p_ataque / 4) * uniform(0.8, 1.2)
                defesa = (self.p_defesa) * 0.1
                object.dano = object.dano - defesa
                self.vida = (self.vida) - object.dano
                if self.vida <= 0:
                    self.vida = 0
                    self.vivo = False
                    print(f'\n{object.nome} derrota {self.nome} com um dano de: {object.dano:.2f}.')
                else:
                    print(f'{object.nome} ataca {self.nome} e inflige: {object.dano:.2f}.')
            cont += 1  # para contagem de turnos
        if cont == x + 1:
            print('\nNenhum Vencedor.')


##            self.hp()
##            object.hp()

def fim_luta():
    x = ' FIM DE LUTA '
    print(f'\n{x:-^19}')


def linha():
    x = '-'
    print(f'{x:-^19}')


def escolha(atacante, defensor, x=100):  # para chamar função através de input
    luta = atacante.ataque(defensor, x)


# criação dos personagens:
esqueleto = Personagem('Esqueleto', 55, 90, 45)
orc = Personagem('Orc', 60, 70, 90)
troll = Personagem('Troll', 75, 65, 85)
enderman = Personagem('Enderman', 75, 75, 60)
zumbi = Personagem('Zumbi', 70, 70, 75)

perso = {'esqueleto': esqueleto, 'orc': orc, 'troll': troll, 'enderman': enderman,
         'zumbi': zumbi}  # dict para chamar variável através de uma string

print('\n' + '-' * 26)
print('Bem-vindo ao jogo da luta!')
print('-' * 26)
input('\nEscolha um personagem, a quantidade de turnos e veja o pau moer.')
info = input('Para saber o nome dos personagens digite "info".').lower()
if info == 'info':
    print('\nPERSONAGENS:\n\tEsqueleto, Orc, Troll, Enderman, Zumbi\n')

valid_qtd = False
valid_nome = False
while valid_qtd == False:  # validar quantidade de turnos
    atc1 = input('Digite a quantidade de turnos:\n')
    if atc1 == 'info':
        print('\nPERSONAGENS:\n\tEsqueleto, Orc, Troll, Enderman, Zumbi\n')
    try:
        x = int(atc1)
        valid_qtd = True
    except:
        print('\nDigite apenas números inteiros.')

while valid_nome == False:  # validar nome atacante 1
    atc1 = input('Digite o nome do atacante:\n').lower()
    if atc1 == 'info':
        print('\nPERSONAGENS:\n\tEsqueleto, Orc, Troll, Enderman, Zumbi\n')
    if atc1 in perso:
        valid_nome = True
    else:
        print('\nEscolha um personagem válido. Para mais informações digite "info".')
valid_nome = False  # validar nome atacante 2
while valid_nome == False:
    atc2 = input('Digite o nome do defensor:\n').lower()
    if atc2 == 'info':
        print('\nPERSONAGENS:\n\tEsqueleto, Orc, Troll, Enderman, Zumbi\n')
    if atc2 in perso:
        if atc2 == atc1:
            print('\nEscolha um personagem diferente. Para mais informações digite "info".')
        else:
            valid_nome = True
    else:
        print('\nDigite um personagem válido. Para mais informações digite "info".')

escolha(perso[atc1], perso[atc2], x)  # excecução da luta
fim_luta()
perso[atc1].hp()
print()
perso[atc2].hp()
linha()

from tkinter import *

janela = Tk()
janela.title('Título da janela')

lb = Label(janela,text='texto da minha janela')
lb.place(x=5,y=5)

janela.mainloop()