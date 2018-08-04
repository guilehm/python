from random import randint


class Jogo:

    def __init__(self):
        self.jogar = True
        self.cows = 0
        self.bulls = 0
        self.tentativas = 1
        self.numero = self.gerar_numero()
        print(self.numero)
        self.chute()
        self.comparar()


    def gerar_numero(self):
        return str(randint(0000, 9999))

    def chute(self):
        self.escolha = str(input('Digite a sua tentativa:\n'))

    def comparar(self):
        self.bulls = 0
        self.cows = 0
        chute = str(self.escolha)
        numero = str(self.numero)

        while self.jogar:
            if chute.isdigit() and len(chute) <= 4:
                try:
                    for i in range(4):
                        if chute[i] == numero[i]:
                            self.bulls += 1
                        else:
                            if chute[i] in numero:
                                self.cows += 1

                    if self.bulls == 4:
                        print('Você ganhou com {} tentativa(s).!\n o número correo é {}.'.format(self.tentativas, self.numero))
                        self.jogar = False
                    else:
                        self.tentativas += 1
                        print('Cows: {}\nBulls: {}\n'.format(self.cows, self.bulls))
                        self.chute()
                        self.comparar()
                except:
                    print('Digite apenas números com 4 dígitos.')
                    self.chute()
                    self.comparar()
            else:
                print('Digite apenas números com 4 dígitos.')
                self.chute()
                self.comparar()

gui = Jogo()
