import json

import requests
from bs4 import BeautifulSoup

r = requests.get('https://ww2.ibge.gov.br/home/estatistica/indicadores/precos/inpc_ipca/ipca-inpc_201807_1.shtm')

soup = BeautifulSoup(r.content, 'html.parser')

print('Title: ', soup.title.get_text())
print('Last IPCA Index:')
bs = soup.find_all('b')

last_ipca = bs[3]
print(last_ipca.get_text())

r = requests.get('https://www2.cetip.com.br/ConsultarTaxaDi/ConsultarTaxaDICetip.aspx')
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())

response = str(soup)
response = json.loads(response)
aliquota = response.get('taxa')
print(aliquota)
