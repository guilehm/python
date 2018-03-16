from random import uniform

class Personagem:
    def __init__(self, nome, vida, p_ataque, p_defesa, arma, frase):
        self.nome = nome
        self.vida = vida
        self.p_ataque = p_ataque
        self.p_defesa = p_defesa
        self.arma = arma
        self.frase = frase

        self.vivo = True
        self.hit = round((self.p_ataque / 4) * uniform(0.9, 1.0), 2)
        self.defesa = round(self.p_defesa * 0.08, 2)

        if self.vida <= 0:
            self.vivo = False

    def stats(self):
        print(f'\nNome: {self.nome}')
        print(f'{self.nome} diz: {self.frase}')
        print(f'HP: {self.vida}')
        # print(f'Arma: {self.arma}')
        # print(f'Ataque: {self.p_ataque}')
        # print(f'Defesa: {self.p_defesa}')

    def ataque(self, object):
        dano = round(self.hit - object.defesa, 2)
        object.vida -= dano
        print(f'{self} recebe um dano de PV {dano} devido ao ataque de {object}')

    def __str__(self):
        return self.nome

batman = Personagem('Batman', 100, 80, 90, 'Boomerangue', 'Eu sou o BATMAN!')
superman = Personagem('Super-Man', 85, 85, 95, 'Raio Laser', 'Ao infinito e além!')
homem_aranha = Personagem('Homem Aranha', 90, 80, 90, 'Teia' ,'Nada temam, o Aracnídeo chegou!')
hulk = Personagem('Hulk', 130, 70, 80, 'Força', 'Hulk esmaga!')

batman.ataque(superman)
superman.stats()

