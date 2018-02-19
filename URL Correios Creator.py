import webbrowser

def calcula_frete (cep_origem, cep_destino, peso, tipo_frete,
                   altura = '10', largura = '20', comprimento = '20'):
    url = 'http://ws.correios.com.br/calculador/CalcPrecoPrazo.aspx?'
    url += '&nCdEmpresa='
    url += '&sDsSenha='
    url += '&nCdServico=' + tipo_frete
    url += '&sCepOrigem=' + cep_origem
    url += '&sCepDestino=' + cep_destino
    url += '&nVlPeso=' + peso
    url += '&nCdFormato=1'
    url += '&nVlComprimento=' + comprimento
    url += '&nVlAltura=' + altura
    url += '&nVlLargura=' + largura
    url += '&nVlDiametro=0'
    url += '&sCdMaoPropria=n'
    url += '&nVlValorDeclarado=0'
    url += '&sCdAvisoRecebimento=n'
    url += '&StrRetorno=xml'
    url += '&nIndicaCalculo=3'

    return url

cep_origem = '01311200'
cep_destino = '01102010'
peso = '0.1'
tipo_frete = '04014'

calculo = calcula_frete(cep_origem, cep_destino, peso, tipo_frete, '30','60','30')
webbrowser.open(calculo, autoraise=True)
