class Personagem:
    def __init__(self, nome, vida, p_ataque, p_defesa, arma, frase):
        self.nome = nome
        self.vida = vida
        self.p_ataque = p_ataque
        self.p_defesa = p_defesa
        self.arma = arma
        self.frase = frase

    def stats(self):
        print(f'Nome: {self.nome}')
        print(f'{self.nome} diz: {self.frase}')
        print(f'HP: {self.vida}')
        print(f'Arma: {self.vida}')
        print(f'Ataque: {self.vida}')
        print(f'Defesa: {self.vida}')