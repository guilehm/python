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
        ingr = ['molho','muçarela','tomate','alho poró','azeitona','pimenta','calabresa','manjericão','bacon','catupiry','presunto','alface',
                'frango','milho','brócolis','alho','cebola','azeite','orégano','oregano','molho de tomate','parmesão','chicória','provolone',
                'ovo','champignon','anchovas','lombo','lombo canadense','rúcula','atum','palmito','parma','salame','gorgonzola',
                'queijo','couve flor','abacaxi','uva passa','chocolate','chocolate branco','açúcar','canela','requeijão',
                'M&Ms','brigadeiro','granulado','morango','sal','prestigio','queijo bri','tomate seco','queijo ralado','escarola','berinjela']
        print('\nDigite o nome dos ingredientes para montar sua pizza.\n\tQuando terminar digite "parar".')
        print('\tO preço de cada ingrediente custa apenas R$ 1,50.')
        parar = False
        global ingredientes
        ingredientes = []

        while parar == False:
            x = input('Escolha um ingrediente:\n').lower()
            if x == 'parar' or x == 'p' or x == 'sair' or x == 's':
                parar = True
            elif x in ingr:
                ingredientes.append((x.lower()))
                print('\n{} adicionado(a)!'.format(x.title()))
            elif x not in ingr:
                print('{} não disponível.'.format(x.lower()))

        ingredientes = sorted(ingredientes)
        print('Os ingredientes escolhidos foram: ')
        print(('INGREDIENTE'.ljust(17)) + ('VALOR ACUMULADO'))
        adicional = float(0)

        for i in ingredientes:
            adicional += 1.49
            print(i.ljust(17) + ('R$ {:.2f}'.format(adicional)))

        print('\nO total de ingredientes é R$ {:.2f}'.format(adicional))
        global adicio
        adicio = adicional

    def pedido(self):
        print('Aqui está sua pizza.')
        print('Esperamos que goste, volte sempre.\n')
        x = input('Deseja imprimir sua fatura?\n')

        if x == 's' or x == 'sim':
            a = 'OBRIGADO POR COMPRAR NA PYZZARIA'
            base = float(39.99)
            print('-'*len(a))
            print(a)
            print(('Volte sempre!').center(len(a)))
            print('-'*len(a))
            print(('Preço base:').ljust(24) + ('R$ 39.99'))
            adicional = float(0)

            for i in ingredientes:
                adicional = 1.49
                print(i.ljust(24).capitalize() + ('R$ {:.2f}'.format(adicional)))
            print('Total ingredientes:'.ljust(24) + 'R$ {:.2f}'.format(adicio))
            print('-'*len(a))
            print('TOTAL PEDIDO:'.ljust(24) + ('R$ {:.2f}'.format(adicio + base)))
            print('-'*len(a))
            print('Siga-nos nas redes sociais.')
            
        else:
            print('Agradecemos sua visita!')
            
                   
user1 = Pizza()
user1.ingredientes()
user1.pedido()













