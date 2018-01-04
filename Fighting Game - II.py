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

    def ataque(self,object):
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

##    def luta(self,ataque,object):
        
        
esqueleto = Personagem('Esqueleto',55,90,45)
orc = Personagem('Orc',60,70,90)
troll = Personagem('Troll',75,65,85)
enderman = Personagem('Enderman',75,75,60)
zumbi = Personagem('Zumbi',70,70,72)

##while orc.vivo == True and esqueleto.vivo == True:
##    if esqueleto.vivo == True and orc.vivo == True:
##        esqueleto.ataque(orc)
##        
##    if orc.vivo == True and esqueleto.vivo == True:
##        orc.ataque(esqueleto)

##while orc.vivo == True and enderman.vivo == True:
##    if enderman.vivo == True and orc.vivo == True:
##        enderman.ataque(orc)
##        
##    if orc.vivo == True and enderman.vivo == True:
##        orc.ataque(enderman)        

##while troll.vivo == True and enderman.vivo == True:
##    if enderman.vivo == True and troll.vivo == True:
##        enderman.ataque(troll)
##        
##    if troll.vivo == True and enderman.vivo == True:
##        troll.ataque(enderman)

##while esqueleto.vivo == True and enderman.vivo == True:
##    if enderman.vivo == True and esqueleto.vivo == True:
##        enderman.ataque(esqueleto)
##        
##    if esqueleto.vivo == True and enderman.vivo == True:
##        esqueleto.ataque(enderman)

while orc.vivo == True and zumbi.vivo == True:
    if zumbi.vivo == True and orc.vivo == True:
        zumbi.ataque(orc)
        
    if orc.vivo == True and esqueleto.vivo == True:
        orc.ataque(zumbi)
    
orc.carac()
##esqueleto.carac()
##troll.carac()
##enderman.carac()
zumbi.carac()
