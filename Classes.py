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
        self.hit = self.p_ataque / 4
        self.defesa = self.p_defesa * 0.08

    def stats(self):
        print(f'\nNome: {self.nome}')
        print(f'{self.nome} diz: {self.frase}')
        print(f'HP: {self.vida:.2f}')
        if self.vivo:
            print(f'{self} está vivo.')
        else:
            print(f'{self} está morto.')

    def ataque(self, object):
        if self.vivo and object.vivo:
            dano = round((self.hit - object.defesa) * uniform(0.7, 1.4), 2)
            object.vida -= dano
            if object.vida <= 0:
                object.vida = 0
                object.vivo = False
            print(f'{self} ataca com {self.arma} e {object} perde {dano} PV.')
        else:
            if self.vivo:
                print('{} está morto'.format(object))
            else:
                print('{} está morto'.format(self))


    def __str__(self):
        return self.nome

batman = Personagem('Batman', 100, 80, 90, 'Boomerangue', 'Eu sou o BATMAN!')
superman = Personagem('Super-Man', 85, 85, 95, 'Raio Laser', 'Ao infinito e além!')
homem_aranha = Personagem('Homem Aranha', 90, 80, 90, 'Teia' ,'Nada temam, o Aracnídeo chegou!')
hulk = Personagem('Hulk', 130, 70, 80, 'Força', 'Hulk esmaga!')

lista = ['batman', 'superman', 'aranha', 'hulk']
personagens = [batman, superman, homem_aranha, hulk]
perso = dict(zip(lista, personagens))
esco = input('Escolha seu personagem\n\t')
lutador = (perso.get(esco.lower()))


