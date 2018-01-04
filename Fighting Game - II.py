from random import randint,uniform

class Personagem():
    def __init__(self,nome,vida,p_ataque,p_defesa):
        self.nome = nome
        self.vida = vida
        self.p_ataque = p_ataque
        self.p_defesa = p_defesa
        self.vivo = True
        
    def carac(self):
        print(f'Nome do personagem: {self.nome}')
        print(f'HP: {self.vida:.2f}')
        print(f'PA: {self.p_ataque}')
        print(f'PD: {self.p_defesa}\n')

    def hp(self):
        print('{}'.format(self.nome).upper())
        print(f'HP: {self.vida:.2f}\n')

    def ataque(self,object,x=100):
        cont = 1
        while self.vivo is True and object.vivo is True and cont <= x:
            if self.vivo is True and object.vivo is True:
                self.dano = (self.p_ataque / 4) * uniform(0.8,1.2)
                defesa = (object.p_defesa) * 0.1
                self.dano = self.dano - defesa
                object.vida = (object.vida)- self.dano
                if object.vida <= 0:
                    object.vida = 0
                    object.vivo = False
                    print(f'{self.nome} derrota {object.nome} com um dano de: {self.dano:.2f}.')
                else:
                    print(f'{self.nome} ataca {object.nome} e inflige: {self.dano:.2f}.')
            if object.vivo is True and self.vivo is True:
                object.dano = (object.p_ataque / 4) * uniform(0.8,1.2)
                defesa = (self.p_defesa) * 0.1
                object.dano = object.dano - defesa
                self.vida = (self.vida)- object.dano
                if self.vida <= 0:
                    self.vida = 0
                    self.vivo = False
                    print(f'{object.nome} derrota {self.nome} com um dano de: {object.dano:.2f}.')
                else:
                    print(f'{object.nome} ataca {self.nome} e inflige: {object.dano:.2f}.')
            cont += 1
        if cont == x+1:
            print('\nNENHUM VENCEDOR.')
            self.hp()
            object.hp()
        
esqueleto = Personagem('Esqueleto',55,90,45)
orc = Personagem('Orc',60,70,90)
troll = Personagem('Troll',75,65,85)
enderman = Personagem('Enderman',75,75,60)
zumbi = Personagem('Zumbi',70,70,75)

troll.ataque(orc,4)
