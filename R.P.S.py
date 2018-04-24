from random import choice

class Jogador:

    def __init__(self, nome):
        self.pontos = 0
        self.nome = nome
        print('Escolha Papel, Pedra ou Tesoura para jogar.\n Para sair digite parar.')

    def joga(self):
        objeto = input('Escolha Pedra, Papel ou Tesoura:\n').lower()
        self.compara(objeto)

    def compara(self, objeto):
        opcoes = ['papel', 'pedra','tesoura']
        bot = choice(opcoes)
        while True:
            if objeto in opcoes:
                if objeto == bot:
                    print('Empate, a máquina escolheu', bot)
                elif objeto == 'pedra':
                    if bot == 'papel':
                        print('Você perdeu, a máquina escolheu Papel')
                        self.pontos -= 1
                    elif bot == 'tesoura':
                        print('Você venceu, a máquina escolheu Tesoura')
                        self.pontos += 1
                elif objeto == 'papel':
                    if bot == 'tesoura':
                        print('Você perdeu, a máquina escolheu Tesoura')
                        self.pontos -= 1
                    elif bot == 'pedra':
                        print('Você venceu, a máquina escolheu Pedra')
                        self.pontos += 1
                elif objeto == 'tesoura':
                    if bot == 'pedra':
                        print('Você perdeu, a máquina escolheu Pedra')
                        self.pontos -= 1
                    elif bot == 'papel':
                        print('Você venceu, a máquina escolheu Papel')
                        self.pontos += 1
            elif objeto == 'parar':
                self.parar()
            else:
                print('Escolha uma opção válida')
                self.joga()

    def parar(self):
        pass

gui = Jogador('Gui')
while True:
    gui.joga()