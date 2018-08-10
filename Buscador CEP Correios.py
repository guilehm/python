import requests

from lxml import etree

URL = "http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaCepEndereco.cfm"


def busca_cep(cep):
    r = requests.post(URL, data=dict(relaxation=cep, tipoCEP="ALL", semelhante="N"))
    tabela = etree.HTML(r.text).find(".//table[@class='tmptabela']")
    logradouro, bairro, cidade_uf, cep = (
        x.text.strip() for x in tabela.findall(".//td")
    )
    cidade, _, uf = cidade_uf.rpartition("/")
    return dict(logradouro=logradouro, bairro=bairro, cidade=cidade, uf=uf, cep=cep)


busca = busca_cep("04110021")
print(busca)
