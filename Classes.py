from random import choice, uniform


class Personagem:
    # Atributos iniciais do objeto
    def __init__(self, nome, vida, p_ataque, p_defesa, arma, frase):
        self.nome = nome
        self.vida = vida
        self.vida_total = vida
        self.p_ataque = p_ataque
        self.p_defesa = p_defesa
        self.arma = arma
        self.frase = frase

        self.vivo = True
        self.hit = self.p_ataque / 4
        self.defesa = self.p_defesa * 0.08

    # Para visualizar os atributos do objeto
    def stats(self):
        # print(f'\nNome: {self.nome}')
        print(f"\n{self.nome} diz: {self.frase}")
        print(f"HP: {self.vida:.2f}", f"- {(self.vida / self.vida_total * 100):.0f}%")
        if self.vivo:
            print(f"{self} está vivo.")
        else:
            print(f"{self} está morto.")

    # Para atacar
    def ataque(self, object):
        if self.vivo and object.vivo:
            dano = round((self.hit - object.defesa) * uniform(0.7, 1.4), 2)
            object.vida -= dano
            if object.vida <= 0:
                object.vida = 0
                object.vivo = False
            print(f"{self} ataca com {self.arma} e {object} perde {dano} PV.")
            input()
        else:
            if self.vivo:
                print("{} está morto".format(object))
            else:
                print("{} está morto".format(self))

    # Retornar nome quando chamar instância
    def __str__(self):
        return self.nome


# escolha do atacante
def escolha(atacante):
    if atacante.lower() in lista:
        print("Você escolheu:", perso.get(atacante))
        return perso.get(atacante)
    else:
        print("Escolha um personagem válido.")
        print("As opções são:\t")
        for i in lista:
            print("-", i.capitalize())
        player = escolha(input("Escolha seu personagem:\n"))
        return player


# escolha aleatória do oponente
def escolha_oponente(atacante):
    oponente = choice(personagens)
    while oponente == atacante:
        oponente = choice(personagens)
    print("Seu oponente é: {}\n".format(oponente))
    return oponente


# Criação de personagens
batman = Personagem("Batman", 100, 80, 90, "Boomerangue", "Eu sou o BATMAN!")
superman = Personagem("Super-Man", 85, 85, 95, "Raio Laser", "Ao infinito e além!")
homem_aranha = Personagem(
    "Homem Aranha", 90, 80, 90, "Teia", "Nada temam, o Aracnídeo chegou!"
)
hulk = Personagem("Hulk", 130, 70, 80, "um soco", "Hulk esmaga!")

# Criação do dicionário para chamar objetos
lista = ["batman", "superman", "homem aranha", "hulk"]
personagens = [batman, superman, homem_aranha, hulk]
dicionario = dict(zip(lista, personagens))

# Escolha manual do atacante e aleatória do defensor
player = escolha(input("Escolha seu personagem:\n"))
bot = escolha_oponente(player)

# Luta
player.ataque(bot)
bot.ataque(player)

# Status
player.stats()
bot.stats()
