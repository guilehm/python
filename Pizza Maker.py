class Pizza():
    
    def __init__(self,formato,borda,tipo_massa,tipo_entrega):
        self.formato = formato
        self.borda = borda
        self.tipo_massa = tipo_massa
        self.tipo_entrega = tipo_entrega

    def carac(self):
        print('O formato da pizza é {}.'.format(self.formato))
        print('A borda é de {}.'.format(self.borda))
        print('A massa é {}.'.format(self.tipo_massa))
        print('Ela será entregue {}.'.format(self.tipo_entrega))

    def ingredientes(self):
        ingr = ['molho','muçarela','tomate','azeitona','calabresa','manjericão','bacon','catupiry','presunto',
                'frango','milho','brócolis','alho','cebola','azeite','orégano','parmesão','chicória','provolone',
                'ovos,','champignon','anchovas','lombo canadense','rúcula','atum','palmito','parma','gorgonzola',
                'queijo','couve flor','abacaxi','uva passa','chocolate','chocolate branco','açúcar','canela',
                'M&Ms','brigadeiro','granulado','morango','prestigio','tomate seco','escarola','berinjela']
        parar = False
        while parar == False:
            x = input('Insira o nome dos ingredientes:\n')
            if x in ingredientes

                        
baiana = Pizza('quadrado','catupiry','integral','assada')
baiana.carac()













