class Personagem:
    def __init__(self, nome, vida, p_ataque, p_defesa, arma, frase):
        self.nome = nome
        self.vida = vida
        self.p_ataque = p_ataque
        self.p_defesa = p_defesa
        self.arma = arma
        self.frase = frase

    def stats(self):
        print(f'\nNome: {self.nome}')
        print(f'{self.nome} diz: {self.frase}')
        print(f'HP: {self.vida}')
        print(f'Arma: {self.arma}')
        print(f'Ataque: {self.p_ataque}')
        print(f'Defesa: {self.p_defesa}')


batman = Personagem('Batman', 100, 80, 90, 'Boomerangue', 'Eu sou o BATMAN!')
batman.stats()

superman = Personagem('Super-Man', 120, 85, 95, 'Raio Laser', 'Ao infinito e além!')
superman.stats()