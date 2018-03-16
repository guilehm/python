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

    def stats(self):
        print(f'\nNome: {self.nome}')
        print(f'{self.nome} diz: {self.frase}')
        print(f'HP: {self.vida}')
        print(f'Arma: {self.arma}')
        print(f'Ataque: {self.p_ataque}')
        print(f'Defesa: {self.p_defesa}')

    def calc_ataque(self):
        self.hit = round((self.p_ataque / 4) * uniform(0.9, 1.0), 2)
        print(self.hit)

    def calc_defesa(self):
        self.defesa = round(self.p_defesa * 0.1, 2)
        print(self.defesa)


batman = Personagem('Batman', 100, 80, 90, 'Boomerangue', 'Eu sou o BATMAN!')
batman.calc_ataque()
batman.calc_defesa()

superman = Personagem('Super-Man', 85, 85, 95, 'Raio Laser', 'Ao infinito e além!')
superman.calc_ataque()
superman.calc_defesa()
