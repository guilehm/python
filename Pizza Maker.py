class Pizza():
    
    def __init__(self):
        self.nome_c = input('Olá, por favor nos informe seu nome: ')
        input('\n{}, seja bem-vindo à Pyzzaria.'.format(self.nome_c.title()))
        input('Escolha apenas os ingredientes que o resto nós cuidamos!')
        #self.nome_p = input('\nEscolha um nome para sua pizza: ')
        #self.formato = input('Escolha entre pizza redonda ou quadrada: ')
        #self.borda = input('Digite sim ou não se deseja borda: ')
        #self.massa = input('Digite o tipo de massa que deseja: ')

    def carac(self):
        print('Olá {}, segue detalhes de seu pedido:'.format(self.nome_p))
        print('O formato da pizza é {}.'.format(self.formato))
        print('A borda é de {}.'.format(self.borda))
        print('A massa é {}.'.format(self.massa))

    def ingredientes(self):
        ingr = ['molho','muçarela','tomate','azeitona','calabresa','manjericão','bacon','catupiry','presunto',
                'frango','milho','brócolis','alho','cebola','azeite','orégano','oregano','molho de tomate','parmesão','chicória','provolone',
                'ovo','champignon','anchovas','lombo','lombo canadense','rúcula','atum','palmito','parma','gorgonzola',
                'queijo','couve flor','abacaxi','uva passa','chocolate','chocolate branco','açúcar','canela',
                'M&Ms','brigadeiro','granulado','morango','prestigio','queijo bri','tomate seco','queijo ralado','escarola','berinjela']
        print('\nDigite o nome dos ingredientes para montar sua pizza.\n\tQuando terminar digite "parar".')
        print('\tO preço de cada ingrediente custa apenas R$ 1,50.')
        parar = False
        ingredientes = []
        while parar == False:
            x = input('Escolha um ingrediente:\n').lower()
            if x == 'parar' or x == 'p':
                parar = True
            elif x in ingr:
                ingredientes.append((x.lower()))
                print('\n{} adicionado(a)!'.format(x.title()))
            elif x not in ingr:
                print('{} não disponível.'.format(x.lower()))
        ingredientes = sorted(ingredientes)
        print('Os ingredientes escolhidos foram: ')
        print(('INGREDIENTE'.ljust(15)) + ('VALOR ACUMULADO'))
        adicional = float(1.5)
        for i in ingredientes:
            print(i.ljust(15) + ('R$ {.:2f}'.format(adicional)))
            adicional += 1.5
        print('\nO total de ingredientes é R$ {.:2f}'.format(adicional))

##        def pedido(self):
##            print('Obrigado por c
                   
baiana = Pizza()
baiana.ingredientes()
baiana.pedido()













